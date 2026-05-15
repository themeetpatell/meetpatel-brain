# What is that?

### **1. Epics**

**Definition**:

An **Epic** is a large body of work that can be broken down into smaller tasks (User Stories) and is usually a significant feature, capability, or overall functionality of the product. Epics often span multiple sprints and require coordination across different teams.

**Characteristics**:

- High-level feature or requirement.
- Broad in scope and objectives.
- Needs to be broken down into smaller User Stories.
- Represents a complete user flow or value proposition.

**Format**:

- **Title**: Concise name that clearly states the Epic’s goal.
- **Description**: A high-level overview of the feature or functionality.
- **Objectives**: Specific goals to be achieved through the Epic.
- **Acceptance Criteria**: Broad criteria that define the success of the Epic.
- **User Impact**: Which users are impacted and how.
- **Dependencies**: Other features or teams that might be involved.
- **Milestones**: Key points or stages to measure progress.

**Example of an Epic**:

- **Title**: Improve Onboarding Experience for Startups
- **Description**: Redesign the onboarding flow for startup users to reduce drop-off rates and improve the overall user experience.
- **Objectives**:
    - Reduce onboarding time by 30%.
    - Increase user engagement in the first session by 50%.
- **Acceptance Criteria**:
    - User flow is streamlined with fewer steps.
    - Integration with third-party sign-ups (e.g., LinkedIn).
    - In-app guidance for better understanding of features.
- **User Impact**: Startup founders registering on the platform.
- **Dependencies**: Integration team for third-party APIs, Design team for UI/UX updates.
- **Milestones**:
    - Research and Requirements Gathering
    - Wireframing and Prototyping
    - Development and Testing
    - Launch and User Feedback Analysis

---

### **2. User Stories**

**Definition**:

A **User Story** is a short, simple description of a feature told from the perspective of the person who desires the new capability, usually a user or customer. User Stories break down Epics into smaller, manageable pieces of work.

**Characteristics**:

- Focused on a single user action or outcome.
- Written in simple, user-centric language.
- Provides context for why the functionality is needed.
- Helps developers and stakeholders understand the user’s perspective.

**Format**:

- **Title**: Brief description of the User Story.
- **User Story**: As a [user role], I want to [goal] so that [benefit].
- **Acceptance Criteria**:
    - **Given**: Preconditions.
    - **When**: User action.
    - **Then**: Expected outcome.
- **Priority**: Level of importance (e.g., High, Medium, Low).
- **Story Points**: Effort estimation for implementation.
- **Dependencies**: Any related stories or technical requirements.

**Example of a User Story**:

- **Title**: Sign-Up with LinkedIn Integration
- **User Story**: As a **Startup Founder**, I want to **sign up using my LinkedIn account** so that **I can quickly create an account without manual data entry**.
- **Acceptance Criteria**:
    - **Given**: The user is on the registration page.
    - **When**: The user clicks on "Sign Up with LinkedIn."
    - **Then**: The user is redirected to LinkedIn for authentication.
    - **And Then**: The user's profile is pre-filled with LinkedIn data.
    - **And Then**: The user is navigated to the onboarding dashboard.
- **Priority**: High
- **Story Points**: 5
- **Dependencies**: LinkedIn API integration, Design of the login page.

---

### **3. Tasks**

**Definition**:

A **Task** is a specific piece of work that needs to be completed as part of a User Story. Tasks are granular and actionable, usually assigned to individual team members and can be completed within a sprint.

**Characteristics**:

- Specific, detailed, and actionable.
- Assigned to a team member for accountability.
- Has a clear definition of done.
- Helps track progress on User Stories.

**Format**:

- **Title**: Concise description of the task.
- **Description**: Detailed explanation of what needs to be done.
- **Assigned To**: Team member responsible for the task.
- **Dependencies**: Other tasks or technical requirements.
- **Effort Estimate**: Time or complexity estimation.
- **Status**: Current status (e.g., To Do, In Progress, Done).

**Example of a Task**:

- **Title**: Integrate LinkedIn OAuth for Sign-Up
- **Description**: Set up LinkedIn OAuth integration for user authentication on the registration page, ensuring it works seamlessly with the existing backend and front-end.
- **Assigned To**: Developer A
- **Dependencies**: Backend setup for user authentication, UI design of the registration page.
- **Effort Estimate**: 8 hours
- **Status**: In Progress

###