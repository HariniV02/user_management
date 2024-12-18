# Final Project: User Management System - Feature 9 

## Implemented Features and Enhancements

### 1. Profile Management 
- Implemented functionality allowing users to update their profile fields such as **name**, **bio**, **location**, and more through a user-friendly API.

**API Endpoint:**
```
/users/updateProfile
```
- Enables users to modify their profile data effortlessly.

**Image:**
![Profile Management Screenshot](photos/Screenshot%202024-12-17%20at%207.13.21%20PM.png)

```

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

- Successful deployment to **DockerHub**:
   - **DockerHub Repository**: [DockerHub Link](https://hub.docker.com/repository/docker/hariniv02/user_management/general)

---

## Testing and Quality Assurance 📊
- **Added 10+ Test Cases:**
   - Comprehensive unit tests implemented to cover profile updates, professional status upgrades, and edge cases.
   - Scenarios include API validation, access control, and successful database updates.

📄 **Link to Test Cases**: [10+ Test Cases](https://github.com/HariniV02/user_management/tree/tests?tab=readme-ov-file)

---



## Issues Resolved 🐞
### Addressed 5 Major Issues to Improve the Project:
1. **Updated Workflow File to Fix Docker Build Issues and Version Control** - [Issue 1 Link](https://github.com/HariniV02/user_management/tree/1-email_verification)
2. **Missing Password Validation During Registration** - [Issue 2 Link](https://github.com/HariniV02/user_management/tree/3-password-validation)
3. **Profile picture URL validation** - [Issue 3 Link](https://github.com/HariniV02/user_management/tree/2-profile-update)
4. **No default role assigned during user creation** - [Issue 4 Link](https://github.com/HariniV02/user_management/tree/4-default-role)
5. **Email Verification** - [Issue 5 Link](https://github.com/HariniV02/user_management/tree/5-docker-build-issues)
📄 **GitHub Issues**: [GitHub Issues Link](https://github.com/HariniV02/user_management/issues)

---

## Reflection Document 📄
Prepare a **1-2 page Word document** summarizing your journey, key learnings, and achievements during the project. Include:
- Links to the closed issues:
   - **5 QA Issues**, **10 Test Cases**, and **1 Feature**.
- Successful deployment details:
   - Link to your DockerHub repository.

**Example Format:**

- [New Test Cases](https://github.com/HariniV02/user_management/tree/tests?tab=readme-ov-file)
- [Feature Implementation](https://github.com/HariniV02/user_management/tree/features?tab=readme-ov-file)
- [DockerHub Link](https://hub.docker.com/repository/docker/hariniv02/user_management/general)

---

