# UTM

### **1. What Are UTM Parameters?**

UTM stands for **Urchin Tracking Module**

- **Where** people came from,
- **How** they got to you,
- And **which campaign** convinced them to click.

---

### **2. The Magic Five (Parameters)**

| **Parameter** | **Purpose** |
| --- | --- |
| **utm_source** | Identifies the referral source—like google, newsletter, or inside-cabs |
| **utm_medium** | Shows the marketing medium—email, cpc, social, video, etc. |
| **utm_campaign** | Labels the specific campaign effort—e.g., summer_sale, offline, or video-sept |
| **utm_term** | Used for paid keywords tracking—works wonders with PPC |
| **utm_content** | Differentiates between multiple links within the same campaign—like blue-button vs. red-button |

**Pro Tip:** Always use utm_source, utm_medium, and utm_campaign. 

---

### **3. Benefits**

- **Precision**: You’ll know whether that lead came from your TikTok video or that fancy email blast.
- **Better Attribution**: UTM-tagged links avoid the dreaded “Direct” traffic in analytics, giving clarity to your efforts .
- **Creative A/B Testing**: If you’re running two versions of a banner, utm_content lets you track which one’s drawing eyeballs.
- **No SEO Overkill**: Google ignores UTMs when crawling—so your rankings stay unshaken .

---

### **4. How to Build**

1. Start with your clean URL:
    
    https://themeetpatel.in/contact
    
2. Add ? and append the core UTMs:
    
    ?utm_source=inside-cabs&utm_medium=video&utm_campaign=offline
    
3. Optional extras:
    - &utm_content=cta-button (to track the exact element clicked)
    - &utm_term=corporate+tax+filing (for keyword granularity)

Full example:

```
https://themeetpatel.in/contact?utm_source=inside-cabs&utm_medium=video&utm_campaign=offline&utm_content=cta-button&utm_term=corporate+tax+filing
```