# Structure of Ecosystem

- Search & Filters

**Tabs:** 

## **1. Information Architecture**

We’re building five card types, but they need a **unified skeleton** so the ecosystem feels cohesive:

- **Shared Elements Across All Cards**
    - Avatar/Logo/Profile Image
    - Name (Company/Person)
    - Short Descriptor (tagline or role)
    - Tags (industry, skills, stage, expertise, etc.)
    - Location (city, country)
    - CTA actions (primary + secondary)

---

## **2. Card Types & Content**

### **Startups Cards**

- **Visual**: Logo on top-left, small verified badge if validated.
- **Info**:
    - Name
    - Tagline (max 1 line, e.g. “AI-powered tax filing for SMBs”)
    - Description (truncated 2 lines, expandable)
    - Tags: sector, funding stage, tech stack
    - Founded On: YYYY
    - Location
- **CTAs**: View Profile | Follow

---

### **Founders Cards**

- **Visual**: Profile photo with a subtle colored ring (active/founder vibe).
- **Info**:
    - Name
    - Role: “Founder @ [Startup Name]”
    - Bio snippet (2 lines: “Ex-Uber | Building SaaS infra”)
    - Tags: expertise, industry
    - Location
- **CTAs**: View Profile | Connect

---

### **Investors Cards**

- **Visual**: Firm logo or personal photo.
- **Info**:
    - Name
    - Role: “Partner @ Sequoia India”
    - Investment thesis tags: FinTech, SaaS, AI
    - Portfolio highlights (mini logos, 3 max)
    - Location
- **CTAs**: View Profile | Follow

---

### **CXOs Cards**

- **Visual**: Professional profile photo, badge for “Fractional CXO.”
- **Info**:
    - Name
    - Role(s): “Fractional CFO, ex-KPMG”
    - Expertise tags (Finance, Ops, Fundraising)
    - Availability status (Open | Busy | Limited)
    - Location
- **CTAs**: View Profile | Invite to Startup

---

### **Employees Cards**

- **Visual**: Profile photo.
- **Info**:
    - Name
    - Role/Skillset: “Growth Marketer” or “UI/UX Designer”
    - Current affiliation (if any)
    - Tags: skills, interests
    - Location
- **CTAs**: View Profile | Hire/Connect

---

## **User Experience Flow**

- **Discovery Grid**: Cards shown in responsive grid, filterable by type (Startup, Founder, Investor, CXO, Employee).
- **Filters & Sorts**: By location, industry, tags, trending, newest.
- **Search**: Smart global search across names, roles, tags.
- **Hover States**: Quick info preview (e.g., # of followers, portfolio count).
- **Profile Deep Dive**: Clicking any CTA → full detailed profile page with social, portfolio, timeline, and contact.

---

## **4. Design Language**

- **Consistency**: All cards same height in grid; typography hierarchy (name bold, role/tagline lighter).
- **Branding**: Tailwind + StartupOS brand colors (neutral base, highlight accents).
- **Micro-interactions**: Follow button animates, hover effects with shadows, tag hover highlights.
- **Badges**: Verified, Featured, Trending for credibility signals.

---

## **5. extra possibilities**

- Mutual connections highlight (“You both follow 3 startups”).
- “Ecosystem Health” bar showing diversity of startups/investors.
- Smart recommendations (AI Copilot suggests people/startups to follow).

---