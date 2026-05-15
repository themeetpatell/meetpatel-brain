# Tech

### **CORE ARCHITECTURE LAYERS**

| **Layer** | **Focus** | **Example Components** |
| --- | --- | --- |
| **1. Identity Layer** | Secure onboarding, profiles, and verification | Firebase Auth, OTP, LinkedIn/Apple login |
| **2. Vision Engine (AI)** | Understand values, goals, & chemistry | GPT-based pitch parser, similarity models |
| **3. Milestone Journey System** | Relationship stages (Seed → Series A → Unicorn) | Milestone state machine, shared goal engine |
| **4. Recommendation Engine** | Dynamic match scoring | Vector embeddings + collaborative filtering |
| **5. Experience Layer (App/Web)** | UI/UX interactions | React Native (mobile), Next.js web app |

### **AI SYSTEM DESIGN**

| **Function** | **AI Model** | **Description** |
| --- | --- | --- |
| **Pitch Understanding** | GPT-4 / fine-tuned model | Analyzes user’s “vision pitch” and extracts values, goals, and energy type |
| **Compatibility Mapping** | Embedding similarity model (Pinecone / OpenSearch) | Matches people based on value alignment and complementary growth patterns |
| **Journey Coach** | LangChain agent | Acts as a personal relationship co-pilot; guides couples with nudges and insights |
| **Emotion & Sentiment Layer** | LLM + NLP models | Tracks emotional tone across chat and voice data for relationship health metrics |
| **AI Personalization** | Recommender + clustering | Adapts user journey, prompts, and milestones dynamically |

### **DATA SYSTEM**

**Database Architecture**

- PostgreSQL: core data (users, milestones, matches)
- ElasticSearch / Pinecone: semantic matching
- Firebase: real-time sync for chat
- S3: media and backup storage
- dbt + Airbyte: for ETL pipelines
- Metabase + Mixpanel: for product analytics

**Data Flow:**

User Input → AI Processing → Match Scoring → Journey Engine → Insights Dashboard

### **FRONTEND & UX SYSTEM**

- **Frontend Frameworks:**
    
    React Native (Mobile) + Next.js (Web)
    
- **Design System:**
    
    Built from scratch in Figma → Tokenized → Synced via Storybook
    
- **Core Modules:**
    - *Pitch Builder* (Onboarding)
    - *Match Deck* (AI-curated profiles)
    - *Journey Hub* (relationship milestones)
    - *Chat + Coach* (AI interaction layer)
    - *Moments Feed* (shared memories)

### **INFRASTRUCTURE & SECURITY**

| **Area** | **Stack / Tool** | **Notes** |
| --- | --- | --- |
| **Cloud Infra** | AWS Amplify + ECS | Hybrid microservices |
| **CI/CD** | GitHub Actions + AWS CodePipeline | Automated build/deploy |
| **Monitoring** | Datadog + PostHog | Real-time usage + error logs |
| **Security** | AES-256 encryption, SOC2 policies | End-to-end encrypted messages |
| **DevOps** | Dockerized apps, auto-scaling clusters | Scalable infra for global user base |