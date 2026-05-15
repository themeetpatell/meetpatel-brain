# Zoho Analytics

## 1 – Getting Started and Creating a Workspace

**Purpose:** Understand what a workspace is, sign up, and import your first data source.

- **What is a workspace?** A workspace acts as a container where you collect different data sources so they can be analysed together. You can add multiple sources (e.g., Zoho CRM, Books, Projects) into one workspace to get a complete picture of your business. Always centralize related data in one workspace.
- **Creating the workspace:** When you import your first data source, the system creates a workspace with the data‑source name. Rename it and add a description to make its purpose clear.
- **Importing data:** Click the **Import Your Data** tab and choose the source (Zoho app, file, database or cloud drive). Start with your CRM so that subsequent apps blend naturally. Select modules/fields you need and set the synchronization interval (hourly sync is the fastest).
- **Adding more sources:** After syncing the first source, use **Add Data Sources** on the left panel to bring in other apps or files. Later sources follow the same process as the first.
- **Cheatcodes:** Use a single workspace per business unit; limit imported fields to what you need; schedule automatic sync (hourly) so your reports stay fresh.

## 2 – Connecting to Data Sources

**Purpose:** Learn about the different types of connectors and how to bring data into Zoho Analytics.

- **Files and feeds:** Zoho Analytics imports CSV, Excel (XLS/XLSX), JSON, TSV, HTML, XML and other tabular files, and even web/URL feeds. You can also set up automatic synchronization.
- **Cloud storage drives:** Upload data directly from cloud services such as Zoho WorkDrive, Google Drive, Microsoft OneDrive, Dropbox and Box.
- **Databases:** Synchronize data from on‑premise or cloud relational databases and NoSQL databases.
- **Business apps:** Connectors exist for apps like Zoho CRM, Salesforce, Microsoft Dynamics, HubSpot, Zoho Bigin and many others. These connectors provide pre‑built reports and dashboards and allow deep analysis.
- **Marketing and survey apps:** Integrate data from Mailchimp, Zoho Campaigns, Google Ads, Google Analytics, SurveyMonkey, Eventbrite and many more. This lets you analyse marketing and survey performance in one place.
- **Cheatcodes:** Always check if a native connector exists before building a manual integration; restrict initial sync to recent data to speed up imports; set cloud‑drive files to auto‑refresh.

## 3 – Data Preparation (Zoho DataPrep)

**Purpose:** Clean and enrich your data before analysis.

- **DataPrep overview:** Zoho DataPrep is an advanced self‑service tool embedded within Zoho Analytics. It lets you prepare large volumes of data from many sources by cleaning and transforming them.
- **Prepare during import:** During import, click **Prepare Data** to open the DataPrep panel. Apply transformations like changing number formats or find‑and‑replace rules, then apply the changes before creating the table. After preparation, review table settings (name, first‑row headers) because date formats and CSV settings cannot be changed later.
- **Prepare existing tables:** If you missed preparation during import, select **View Data Quality** or **Prepare Data** from the table’s **More** menu. View data quality, then open the preparation pane to perform transformations.
- **Data quality bar:** DataPrep displays a bar for each column showing valid (green), invalid (red) and missing (grey) values. Clicking a section filters the dataset so you can fix invalid or missing values quickly.
- **Sample strategies:** For large datasets, DataPrep offers sampling methods (initial rows, random sample, erroneous sample or column‑based sample) to analyse subsets of data.
- **Histogram and column details:** Histograms show the distribution of values; the side panel lists data type, unique values, and counts of valid/invalid/missing entries, and lets you change data types.
- **Cheatcodes:** Use the data quality bar to pinpoint problem columns; apply find‑and‑replace to fix common data entry errors; choose sampling to speed up transformations; always correct data types before building reports.

## 4 – Data Modelling & Relationships

**Purpose:** Understand how tables are linked and how to use Auto‑Join and lookup columns.

- **Joining tables:** To combine data from multiple tables, Zoho Analytics offers **Auto‑Join** or **Query Tables**.
- **Lookup columns:** Define a lookup relationship between tables using a common column. In the **Sales** example, the `Sales Person ID` column in `Sales` and `Sales Person` tables forms a relationship. Once a lookup is defined, Auto‑Join automatically joins the tables when you create reports.
- **Defining lookups:** You can define lookups during import (via the **Join tables** option), in the table designer (change a column to a lookup), or by editing the design. Zoho Analytics suggests possible lookups based on column names and data types.
- **Creating reports with Auto‑Join:** After defining lookups, create a chart; the report editor will list columns from related tables. Drag columns from different tables and Zoho Analytics automatically joins them to generate the report.
- **Cheatcodes:** Define lookup relationships as soon as you import data; ensure that join columns have unique IDs; rely on Auto‑Join for most multi‑table reports; avoid cartesian joins and duplicate values to prevent inaccurate results.

## 5 – Query Tables & SQL

**Purpose:** Use SQL to transform and combine data when Auto‑Join isn’t enough.

- **Query table concept:** A query table lets you create a new data view by combining data from one or more tables using the SQL **SELECT** statement. The resulting data view behaves like a normal table – you can build reports, share it or even create another query table over it.
- **When to use query tables:** Use them for advanced transformations such as filtering datasets, uniting tables (UNION), applying SQL functions, joining datasets and creating custom calculations. Avoid them for simple calculations or joins; formulas and auto‑join handle those needs.
- **Best practices:**
    - Don’t create separate query tables for each small use case; combine metrics in one table.
    - Avoid using `SELECT *`; select only columns you need.
    - Ensure proper join conditions and avoid cartesian joins.
    - Use `GROUP BY` only on non‑aggregate columns, and don’t group by too many columns.
    - Regularly clean up unused query tables to improve performance.
- **Cheatcodes:** Test your SQL on small samples; use formulas for simple metrics; reference lookup columns for joins; start queries with specific column lists; keep query tables organised in folders.

## 6 – Creating Reports & Visualizations

**Purpose:** Build charts, pivot tables, summary reports and KPI widgets.

- **Chart basics:** After you drop fields onto the appropriate shelves, click the **Settings** icon to open the settings pane. This pane includes **General**, **Analysis** and **Applied Settings** tabs.
- **General settings:** Customize titles, descriptions and how to handle missing values. You can choose to display unknown or missing values and select a chart effect.
- **Overview effect:** For charts with many data points, enable the overview effect to add a small preview below the chart. Use the slider to focus on a specific region. The brush effect lets you highlight and explore selected data ranges.
- **Axis settings:** Customize labels, fonts and colors for X and Y axes; adjust tick mark orientation (horizontal, vertical or slanting) and specify scales (linear, logarithmic or square‑root). You can also set ranges and intervals.
- **Borders and colors:** Apply different border styles, grid lines, marker fill colors and background colors to enhance readability.
- **Cheatcodes:** Keep chart titles short and descriptive; use the overview effect for long time‑series; adjust axis scales to highlight trends; use contrasting colors to differentiate series; add threshold lines to show targets; enable drill‑down or drill‑through for detailed analysis.

## 7 – Designing Interactive Dashboards

**Purpose:** Combine multiple reports into interactive dashboards for decision‑making.

- **Dashboard concept:** A dashboard combines charts, pivot tables, KPI widgets and text on a single page. Zoho Analytics provides a flexible grid layout (m×n) to arrange components and create visually rich, interactive dashboards.
- **Creating a dashboard:** Click **Create > New Dashboard** to open the dashboard designer. Drag reports from the left panel into the design area; you can add as many reports as needed and resize them to fit.
- **Adding tabs:** You can add up to 10 tabs to organise content. In the dashboard designer, click **Add Tab**, rename or duplicate tabs, or delete them.
- **Organising components:** Use drag‑and‑drop to rearrange components. To resize, drag borders or use copy dimensions, fit‑to‑width or fill‑space options. You can resize multiple components together.
- **KPI widgets & user filters:** Add KPI widgets to display key metrics at a glance. Use user filters (drop‑downs, lists, timeline filters) to let viewers slice data by region, date or other dimensions. Merge filters across reports for a unified filter control.
- **Cheatcodes:** Keep dashboards uncluttered; group related charts and KPIs; use consistent sizing; add descriptive text or images for context; provide user filters at the top for interactivity; duplicate tabs to compare scenarios.

## 8 – Using Ask Zia & Augmented Analytics

**Purpose:** Leverage natural‑language queries and AI‑powered insights.

- **Conversation mode:** Ask Zia allows you to chat with an AI assistant to get reports. Activate conversation mode from the **Ask Zia** tab, the **Workspace Search** or the **Dashboard** page. Zia understands natural‑language questions and returns the best possible report or leads you to relevant help documentation.
- **Chat & reports:** You can ask Zia basic questions or chitchats. For analytics, specify the metric or dimension you want, and Zia generates a report. As you ask follow‑up questions, it appends to the query. Use **double enter** or type **“Clear”** to start a new conversation.
- **Auto suggestions:** Zia suggests questions and relevant columns based on your data while you type.
- **OpenAI integration:** With OpenAI integration, you can ask Zia to create formulas or queries. Type “Create a formula” or “Help me with a query”; Zia will propose a formula or SQL code. You can copy it, open it in the editor, modify it or save it as a new column or query table.
- **Zia Insights:** After generating a report, click the Zia icon or type “Insights” to get a narrative summary of your report.
- **Cheatcodes:** Ask for specific metrics (“show total sales by month”); include filters (“…for 2025”); use Zia’s suggestions for ideas; test formulas in a small workspace before saving; use OpenAI integration to draft complex formulas; rate Zia’s responses to improve suggestions.

## 9 – Sharing, Publishing & Collaboration

**Purpose:** Distribute reports and dashboards securely.

- **Easy sharing:** You can share data, reports or dashboards with any user or group; recipients access the same live views online.
- **Controlled data access:** Apply row‑level filters and select columns so shared users see only what they need. Set fine‑grained permissions (read, write, export, share) so users perform only allowed actions.
- **Single version of truth:** Shared reports always show the latest data; there are no conflicting file versions.
- **Collaborative analysis:** Zoho Analytics allows multiple people to analyse the same data and make decisions collectively.
- **Secure sharing:** You can require recipients to log in (private sharing) or allow public access without login.
- **Cheatcodes:** Create groups for teams (sales, marketing) and share dashboards with the whole group; schedule reports to be emailed regularly; embed dashboards in intranet or websites; use comments to discuss insights within the platform.

## 10 – Putting It All Together: Best Practices & Teaching Tips

Use these recommendations to reinforce learning and ensure students become confident users:

- **Start with clean data:** Encourage learners to use DataPrep during import and fix quality issues early. Show how the data quality bar highlights invalid or missing values.
- **Define relationships first:** Establish lookup relationships as soon as data is imported to enable Auto‑Join.
- **Use formulas for simple metrics:** Teach students that formulas are faster than query tables for basic calculations.
- **Choose the right chart:** Discuss when to use bar, line, pie or map charts. Show how to customize axes and add overview effects.
- **Build interactive dashboards:** Emphasize drag‑and‑drop design, user filters, KPI widgets and tabbed layouts.
- **Leverage Ask Zia:** Encourage natural‑language queries and show how Zia Insights provide narrative interpretations.
- **Control access:** Demonstrate how to share reports securely with row‑level filters and proper permissions.
- **Iterate and refine:** After building reports and dashboards, review them with stakeholders, get feedback and make improvements. Regularly clean up unused query tables and workspaces to maintain performance.

[](https://www.google.com/s2/favicons?domain=https://www.zoho.com&sz=32)

[](https://www.google.com/s2/favicons?domain=https://zenatta.com&sz=32)