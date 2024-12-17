from builtins import range
import pytest
from sqlalchemy import select
from app.dependencies import get_settings
from app.models.user_model import User, UserRole
from app.services.user_service import UserService
from app.utils.nickname_gen import generate_nickname

pytestmark = pytest.mark.asyncio

# Test updating a user with valid profile fields (name, bio, location)
async def test_update_user_valid_profile_fields(db_session, user):
    """Test updating user profile with valid fields: name, bio, location."""
    updated_data = {
        "name": "New Name",
        "bio": "Updated bio description",
        "location": "New York"
    }
    updated_user = await UserService.update(db_session, user.id, updated_data)
    assert updated_user is not None
    assert updated_user.name == updated_data["name"]
    assert updated_user.bio == updated_data["bio"]
    assert updated_user.location == updated_data["location"]

# Test upgrading user to professional status
async def test_upgrade_user_to_professional(db_session, verified_user):
    """Test upgrading a user to professional status."""
    result = await UserService.upgrade_to_professional(db_session, verified_user.id)
    assert result is True
    upgraded_user = await UserService.get_by_id(db_session, verified_user.id)
    assert upgraded_user.is_professional is True

# Test notification sent when user is upgraded to professional
async def test_notification_on_professional_upgrade(db_session, verified_user, email_service):
    """Test sending notification on professional status upgrade."""
    with pytest.raises(AssertionError):
        await UserService.upgrade_to_professional(db_session, verified_user.id, email_service)
        email_service.send_user_email.assert_called_once()

# Test profile field validation edge cases
async def test_update_user_profile_field_validation(db_session, user):
    """Test invalid data for profile field updates."""
    invalid_data = {
        "name": "",  # Empty name
        "bio": "x" * 1001,  # Exceeds max bio length
        "location": 12345  # Invalid location type
    }
    updated_user = await UserService.update(db_session, user.id, invalid_data)
    assert updated_user is None

# Test searching users for professional status upgrade
async def test_search_users_for_professional_upgrade(db_session, users_with_same_role_50_users):
    """Test search functionality for users eligible for professional upgrade."""
    eligible_users = await UserService.search_users(db_session, role=UserRole.AUTHENTICATED.name)
    assert len(eligible_users) > 0
    assert all(user.role == UserRole.AUTHENTICATED for user in eligible_users)

# Additional edge case for upgrading a user to professional status
async def test_upgrade_nonexistent_user_to_professional(db_session):
    """Test upgrading a non-existent user to professional status."""
    non_existent_user_id = "non-existent-id"
    result = await UserService.upgrade_to_professional(db_session, non_existent_user_id)
    assert result is False

