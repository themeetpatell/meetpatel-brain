# SOP

**Purpose**

- To establish a structured and efficient process for managing sprints, ensuring timely delivery of high-quality product increments.
- To foster collaboration, transparency, and continuous improvement within the development team.

**Sprint Duration**

- **Standard Sprint Length:** Two weeks (10 working days).

<aside>
💡

**Flexibility:** The sprint duration may be adjusted based on project needs and team velocity but as of now we will be running for two week sprints.

</aside>

**Team Load:**

- **Capacity Planning:** Conduct a sprint capacity planning session before each sprint, considering:
    - Team Members' **Availability, Skill Sets & Expertise** and their **Historical Velocity**
- **Realistic Commitment:** The team should commit to a workload that can be confidently completed within the sprint duration.

**Product Priority**

- **Backlog Refinement:**
    - Hold regular backlog refinement sessions (at least once per sprint) to review, clarify, and estimate user stories.
    - Prioritize user stories based on the MoSCoW framework, client feedback, and strategic alignment.
    - Ensure stories are "Ready for Development" before sprint planning.
    - **"Ready" Definition:**
        - Is it clear & concise? Description and requirement documentation
        - Acceptance criteria?
        - Dependencies? None identified
        - Estimated? X story points
- **Sprint Goals:**
    - Define clear and measurable sprint goals that contribute to the overall product roadmap and deliver value to clients.
    - Communicate sprint goals clearly to the team and stakeholders.
- **To be conducted on: First day**

**Task Grooming Process**

- **Task Breakdown:**
    - Decompose user stories into smaller, actionable items in Jira.
    - Ensure each task has a clear description, acceptance criteria, and assignee, priority, and story points. *Also in some cases, product preposition written by an engineer, how exactly that engineer is proposing to build that.*
    - **Standard Template for story:** Utilize a consistent user story template to capture essential information:
        - As a **[user role],** I want to **[goal]** so that **[benefit]**.
        - **Example:** As a **Startup Founder**, I want to **find a fractional CFO with experience in fundraising and financial planning** so that **I can secure funding and manage my startup’s finances effectively without the high cost of a full-time hire**.
- **Estimation:**
    - Use story points for relative estimation of task complexity and effort.
    - Conduct collaborative estimation sessions (e.g., Planning Poker) to leverage collective knowledge and reach consensus.
- **Dependencies:**
    - Identify and document any dependencies between tasks to ensure proper sequencing and avoid blockers.
    - Utilize Jira's dependency management features to visualize and track dependencies.

**Story Point per Task**

- **Story Point Scale:** We will be following Fibonacci story point scale consistently. (e.g., Fibonacci sequence: 1, 2, 3, 5, 8, 13, etc.).
- **Examples:**
    - 1: Add a tooltip or help text to a specific field.
    - 2: Add a new filter or sorting option to a data table.
    - 3: Develop a new chart or visualization on the dashboard or Implement a basic integration with a third-party API.
    - 5: Build a new feature that involves multiple components and interactions (e.g., a custom report builder).
    - 8: Develop a major new feature that requires significant backend development and testing (e.g., tax filing assistance).

---

**Task Assignment**

- **Ownership & Accountability:** Clearly assign each task to a single owner who is responsible for its completion.
- **Skill Matching:** Assign tasks based on team members' skills, expertise, and interests.
- **Workload Balancing:** Distribute tasks evenly across team members, considering their individual capacity and availability.

---

**Task Quality Assurance and Execution**

- **Acceptance Criteria:** Define clear and specific acceptance criteria for each user story to establish a shared understanding of what constitutes "done."
    
    **Scenario:**
    
    - **Given:** [Precondition(s)]The startup founder is logged into the Strategix platform and has completed their profile, specifying their needs and stage of business.
    - **When:** [User action] The founder searches for a fractional CFO on the platform and applies filters such as industry experience, fundraising expertise, and availability.
    - **Then:** [Expected outcome] The platform displays a list of vetted CFO candidates who match the criteria, complete with profiles, ratings, previous experience, and expected compensation rates.
- **Code Reviews:** Conduct thorough code reviews to ensure code quality, maintainability, and adherence to coding standards.
- **Testing:** Implement a robust testing strategy, including unit tests, integration tests, and end-to-end tests, both manual and automated.
- **Continuous Integration:** Leverage Jira's integration with your CI/CD pipeline to automate builds, tests, and deployments, enabling early detection and resolution of issues.

---

**Sprint Ceremonies**

- **Sprint Planning meeting:**
    - Product priority, Team load and task grooming process, story points per tasks, task assignments
    - Break down user stories into tasks, estimate effort, and assign ownership.
- **Daily Standups:**
    - Hold brief daily standups to track progress, identify blockers, and ensure team alignment.
    - Focus on what was done yesterday, what will be done today, and any obstacles.
- **Sprint Review:**
    - Demonstrate the completed work to stakeholders at the end of the sprint.
    - Gather feedback and incorporate it into future sprints.
- **Sprint Retrospective:**
    - Reflect on the sprint, identify areas for improvement, and develop action plans to implement changes in the next sprint.