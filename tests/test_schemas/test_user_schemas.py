import uuid
import pytest
from pydantic import ValidationError
from datetime import datetime
from app.schemas.user_schemas import UserBase, UserCreate, UserUpdate, UserResponse, UserListResponse, LoginRequest
from app.models.user_model import UserRole

# Fixtures for common test data
@pytest.fixture
def user_base_data():
    return {
        "nickname": "john_doe_123",
        "email": "john.doe@example.com",
        "first_name": "John",
        "last_name": "Doe",
        "role": "AUTHENTICATED",
        "bio": "I am a software engineer with over 5 years of experience.",
        "profile_picture_url": "https://example.com/profile_pictures/john_doe.jpg",
        "linkedin_profile_url": "https://linkedin.com/in/johndoe",
        "github_profile_url": "https://github.com/johndoe"
    }

@pytest.fixture
def user_create_data(user_base_data):
    return {**user_base_data, "password": "SecurePassword123!"}

@pytest.fixture
def user_update_data():
    return {
        "email": "john.doe.new@example.com",
        "nickname": "j_doe",
        "first_name": "John",
        "last_name": "Doe",
        "bio": "I specialize in backend development with Python and Node.js.",
        "profile_picture_url": "https://example.com/profile_pictures/john_doe_updated.jpg"
    }

@pytest.fixture
def user_response_data(user_base_data):
    return {
        "id": uuid.uuid4(),
        "nickname": user_base_data["nickname"],
        "first_name": user_base_data["first_name"],
        "last_name": user_base_data["last_name"],
        "role": user_base_data["role"],
        "email": user_base_data["email"],
        "links": []
    }

@pytest.fixture
def login_request_data():
    return {"email": "john_doe_123@emai.com", "password": "SecurePassword123!"}

# Tests for UserBase
def test_user_base_valid(user_base_data):
    user = UserBase(**user_base_data)
    assert user.nickname == user_base_data["nickname"]
    assert user.email == user_base_data["email"]

# Tests for UserCreate
def test_user_create_valid(user_create_data):
    user = UserCreate(**user_create_data)
    assert user.nickname == user_create_data["nickname"]
    assert user.password == user_create_data["password"]

# Tests for UserUpdate
def test_user_update_valid(user_update_data):
    user_update = UserUpdate(**user_update_data)
    assert user_update.email == user_update_data["email"]
    assert user_update.first_name == user_update_data["first_name"]

# Tests for UserResponse
def test_user_response_valid(user_response_data):
    user = UserResponse(**user_response_data)
    assert user.id == user_response_data["id"]

# Tests for LoginRequest
def test_login_request_valid(login_request_data):
    login = LoginRequest(**login_request_data)
    assert login.email == login_request_data["email"]
    assert login.password == login_request_data["password"]

# Parametrized tests for nickname and email validation
@pytest.mark.parametrize("nickname", ["test_user", "test-user", "testuser123", "123test"])
def test_user_base_nickname_valid(nickname, user_base_data):
    user_base_data["nickname"] = nickname
    user = UserBase(**user_base_data)
    assert user.nickname == nickname

@pytest.mark.parametrize("nickname", ["test user", "test?user", "", "us"])
def test_user_base_nickname_invalid(nickname, user_base_data):
    user_base_data["nickname"] = nickname
    with pytest.raises(ValidationError):
        UserBase(**user_base_data)

# Parametrized tests for URL validation
@pytest.mark.parametrize("url", ["http://valid.com/profile.jpg", "https://valid.com/profile.png", None])
def test_user_base_url_valid(url, user_base_data):
    user_base_data["profile_picture_url"] = url
    user = UserBase(**user_base_data)
    assert user.profile_picture_url == url

@pytest.mark.parametrize("url", ["ftp://invalid.com/profile.jpg", "http//invalid", "https//invalid"])
def test_user_base_url_invalid(url, user_base_data):
    user_base_data["profile_picture_url"] = url
    with pytest.raises(ValidationError):
        UserBase(**user_base_data)

# Parametrized tests for password validation
@pytest.mark.parametrize("password", [
    "Secure*1234",       # Contains uppercase, lowercase, digit, special character, and meets length requirement
    "MySecure$456",      # Meets all conditions
    "Valid@2021Test",    # Meets all conditions
    "!Strong1Password",  # Meets all conditions
])
def test_password_valid(password, user_create_data):
    user_create_data["password"] = password
    user = UserCreate(**user_create_data)
    assert user.password == password

@pytest.mark.parametrize("password", [
    "short",             # Too short
    "nouppercase1!",     # Missing uppercase letter
    "NOLOWERCASE1!",     # Missing lowercase letter
    "NoSpecial12345",    # Missing special character
    "NoDigit!Password",  # Missing digit
])
def test_password_invalid(password, user_create_data):
    user_create_data["password"] = password
    with pytest.raises(ValidationError):
        UserCreate(**user_create_data)

# Tests for UserCreate role defaults and explicit assignment
def test_user_create_with_default_role(user_create_data):
    user_create_data.pop("role", None) 
    user = UserCreate(**user_create_data)
    assert user.role == UserRole.AUTHENTICATED

def test_user_create_with_explicit_role(user_create_data):
    user_create_data["role"] = UserRole.ADMIN
    user = UserCreate(**user_create_data)
    assert user.role == UserRole.ADMIN
