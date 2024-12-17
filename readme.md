# Final Project: User Management System - Feature 9 

## Implemented Features and Enhancements

### 1. Profile Management 
- Implemented functionality allowing users to update their profile fields such as **name**, **bio**, **location**, and more through a user-friendly API.

**API Endpoint:**
```
/users/updateProfile
```
- Enables users to modify their profile data effortlessly.

---

### 2. User Status Upgrade 
- Developed functionality for managers and admins to upgrade a user's status to **"professional"**.

**API Endpoint:**
```
/users/{user_id}/updateToProfessional
```
- Empowers managers and admins to manage user designations effectively.

---

### 3. Email Notification System ✉️
- Added automatic email notifications to inform users when their status is upgraded to **"professional"**, ensuring they are kept in the loop.

---

## Technical Updates and Deployment 🛠️
- To resolve CI/CD pipeline failures and ensure smooth deployment, the following dependencies were updated:
   - **PyMySQL** `>=1.1.1`
   - **starlette** `>=0.40.0`
   - **fastapi** `>=0.103.0`

- Successful deployment to **DockerHub**:
   - **DockerHub Repository**: [DockerHub Link](https://hub.docker.com/repository/docker/hariniv02/user_management/general)

---

## Testing and Quality Assurance 📊
- **Added 10+ Test Cases:**
   - Comprehensive unit tests implemented to cover profile updates, professional status upgrades, and edge cases.
   - Scenarios include API validation, access control, and successful database updates.

📄 **Link to Test Cases**: [10+ Test Cases](https://github.com/HariniV02/user_management/tree/tests?tab=readme-ov-file)

---

## Code and Test Details 📈
- **Feature 9 Implementation**: [GitHub Repository Link](https://github.com/your-repo)

---

## Test Cases Implemented for Feature 9 ✅
Here are the test cases that validate the **Profile Management** and **User Status Upgrade** features:

### 1. Profile Field Updates
**File**: `tests/test_services/test_user_service.py`
```python
async def test_update_user_valid_profile_fields(db_session, user):
    """Test updating user profile with valid fields: name, bio, location."""
    updated_data = {
        "name": "New Name",
        "bio": "Updated bio description",
        "location": "New York"
    }
    updated_user = await UserService.update(db_session, user.id, updated_data)
    assert updated_user.name == updated_data["name"]
    assert updated_user.bio == updated_data["bio"]
    assert updated_user.location == updated_data["location"]
```

### 2. Profile Field Validation
**File**: `tests/test_services/test_user_service.py`
```python
async def test_update_user_profile_field_validation(db_session, user):
    """Test invalid fields during profile update."""
    invalid_data = {
        "name": "",            # Invalid name
        "bio": "x" * 1001,     # Bio too long
        "location": 12345      # Invalid location type
    }
    updated_user = await UserService.update(db_session, user.id, invalid_data)
    assert updated_user is None, "Invalid fields should fail the update process"
```

### 3. Professional Status Upgrade
**File**: `tests/test_services/test_user_service.py`
```python
async def test_upgrade_user_to_professional(db_session, user):
    """Test upgrading a user to professional status."""
    result = await UserService.upgrade_to_professional(db_session, user.id)
    assert result is True
    upgraded_user = await UserService.get_by_id(db_session, user.id)
    assert upgraded_user.is_professional is True
```

### 4. Notifications on Professional Upgrade
**File**: `tests/test_services/test_user_service.py`
```python
async def test_notification_on_professional_upgrade(db_session, user, email_service):
    """Test that a notification email is sent when a user is upgraded to professional."""
    await UserService.upgrade_to_professional(db_session, user.id, email_service)
    email_service.send_user_email.assert_called_once_with(
        user.email,
        subject="Congratulations! You're now a Professional User",
        message="Your status has been upgraded to Professional!"
    )
```

### 5. Search for Users Eligible for Upgrade
**File**: `tests/test_services/test_user_service.py`
```python
async def test_search_users_for_professional_upgrade(db_session, users_with_same_role_50_users):
    """Test filtering users eligible for professional upgrade."""
    search_results = await UserService.search_users(db_session, role=UserRole.AUTHENTICATED, limit=10)
    assert len(search_results) == 10
    for user in search_results:
        assert user.role == UserRole.AUTHENTICATED
```

---

## Issues Resolved 🐞
### Addressed 5 Major Issues to Improve the Project:
1. **Updated Workflow File to Fix Docker Build Issues and Version Control** - [Issue 1 Link](https://github.com/your-repo/issues/1)
2. **Missing Password Validation During Registration** - [Issue 2 Link](https://github.com/your-repo/issues/2)

📄 **GitHub Issues**: [GitHub Issues Link](https://github.com/your-repo/issues)

---

## Reflection Document 📄
Prepare a **1-2 page Word document** summarizing your journey, key learnings, and achievements during the project. Include:
- Links to the closed issues:
   - **5 QA Issues**, **10 Test Cases**, and **1 Feature**.
- Successful deployment details:
   - Link to your DockerHub repository.

**Example Format:**
- [QA Issue 1](https://github.com/your-repo/issues/1)
- [New Test Case 1](https://github.com/your-repo/issues/2)
- [Feature Implementation](https://github.com/your-repo/issues/3)
- [DockerHub Link](https://hub.docker.com/repository/docker/hariniv02/user_management/general)

---

## Submission Checklist ✅
- [ ] **Reflection Document**: Includes links to all required issues and the DockerHub repository.
- [ ] **Implemented Feature**: Completed and functional.
- [ ] **Commit History**: Minimum 10 commits with clear commit messages.
- [ ] **DockerHub Deployment**: Project deployed successfully.
- [ ] **Tests Passing**: All automated tests pass on GitHub Actions.