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
   - **DockerHub Repository**: [DockerHub Link](https://hub.docker.com/repository/docker/username/repository)

---

## Testing and Quality Assurance 
- **Added 10+ Test Cases:**
   - Comprehensive unit tests implemented to cover profile updates, professional status upgrades, and edge cases.
   - Scenarios include API validation, access control, and successful database updates.

📄 **Link to Test Cases**: [10+ Test Cases](https://github.com/your-repo/issues/1)

---

## Code and Test Details 
- **Feature 9 Implementation**: [GitHub Repository Link](https://github.com/your-repo)

---

## Issues Resolved 
### Addressed 5 Major Issues to Improve the Project:
1. **Updated Workflow File to Fix Docker Build Issues and Version Control** - [Issue 1 Link](https://github.com/your-repo/issues/1)
2. **Missing Password Validation During Registration** - [Issue 2 Link](https://github.com/your-repo/issues/2)

📄 **GitHub Issues**: [GitHub Issues Link](https://github.com/your-repo/issues)

---

## Reflection Document 
Prepare a **1-2 page Word document** summarizing your journey, key learnings, and achievements during the project. Include:
- Links to the closed issues:
   - **5 QA Issues**, **10 Test Cases**, and **1 Feature**.
- Successful deployment details:
   - Link to your DockerHub repository.

**Example Format:**
- [QA Issue 1](https://github.com/your-repo/issues/1)
- [New Test Case 1](https://github.com/your-repo/issues/2)
- [Feature Implementation](https://github.com/your-repo/issues/3)
- DockerHub Repository: [DockerHub Link](https://hub.docker.com/repository/docker/username/repository)

---

## Commit History 
Ensure you have **10+ meaningful commits**:
- Use professional, descriptive commit messages.
- Showcase progress and dedication throughout the project.

> Projects with **less than 10 commits** will receive an automatic **0**.

---

## Submission Checklist 
- [ ] **Reflection Document**: Includes links to all required issues and the DockerHub repository.
- [ ] **Implemented Feature**: Completed and functional.
- [ ] **Commit History**: Minimum 10 commits with clear commit messages.
- [ ] **DockerHub Deployment**: Project deployed successfully.
- [ ] **Tests Passing**: All automated tests pass on GitHub Actions.


