import streamlit as st
import time




# Tabs for navigation
tabs = st.tabs([
    "Introduction",
    "Data Preparation",
    "Chapter 1: Chat Activity Over Time",
    
    "Chapter 2: Chat Response Times",
    "Chapter 3: Chat Patterns",
    "Chapter 4: Word Analysis",
    "Conclusion"
])

    

# Function to scroll to the section
def navigate_to_section(section_id):
    st.markdown(f"<a id='{section_id}'></a>", unsafe_allow_html=True)

# Introduction Section
with tabs[0] :

 st.title("📊 My WhatsApp Conversations – A Data-Driven Journey")
 st.subheader("What do my chats reveal about me? Let’s explore!")

 # Dynamic Counter for Stats
 total_messages = 88002
 total_words = 497793
 total_hours = 366

 st.markdown("### Key Stats")
 col1, col2, col3 = st.columns(3)
 for col, metric, label in zip(
    [col1, col2, col3], 
    [total_messages, total_words, total_hours], 
    ["Total Messages", "Total Words", "Total Hours Chatting"]
 ):
    with col:
        placeholder = st.empty()
        for i in range(0, metric, max(1, metric // 100)):
            placeholder.metric(label, i)
            time.sleep(0.01)
        placeholder.metric(label, metric)

with tabs[1] :
  # 1. Data Collection
 st.header("1️⃣ Data Collection")
 st.markdown("""
 - The data was collected from exported **WhatsApp chat files**.  
 - Each file was structured in a **message format with timestamps, senders, and message content.**  
 """)

 # 2. Data Cleaning
 st.header("2️⃣ Data Cleaning")
 st.markdown("""
 - Cleaned inconsistencies, including:
  - **Timestamp formatting:** Converted to uniform date-time objects.
  - **Sender names:** Standardized variations and nicknames.
   -  Removed **Media Omitted** message which was replacing all media sent.
  - **Special cases:** Removed system-generated messages (e.g., "Missed Voice Call")
 
   
 - **Outcome:** Clean and consistent data for further analysis.
 """)

 # 3. Data Pre-Processing
 st.header("3️⃣ Data Pre-Processing")
 st.markdown("""
 To prepare for analysis, we performed:  
 - **Feature Engineering:**  
  - Total messages by each person.  
  - Percentage of messages sent by me.  
  - Average message length.  
  - Average response time.  
  - Unique days of chat activity.  
 - **Categorization:** Split chats into `friend`, `work`, and `junior` categories based on context and contact groups.  
 - **Data Transformation:** Categorical features were encoded as binary variables for modeling.
 """)
with tabs[2] :
 # Chapter 1: Chat Activity Over Time
 st.header("📊 Chapter 1: How Active Am I?")
 st.subheader("Let’s start by looking at my chat activity on different days of the week.")
 st.image("screenshots/weekday.png")
 st.markdown(
    "Monday kicks off with a surge in messages, perhaps fueled by weekend catch-ups and fresh conversations. "
    "However, as the week progresses, a noticeable dip occurs on Tuesday—possibly due to midweek work or study routines taking over. "
    "Wednesday and Thursday show a steady recovery before a dramatic drop on Friday, when people might be winding down and preparing for the weekend. "
    "But Saturday brings a strong resurgence in activity, hinting at social plans and casual chats, before gradually tapering off on Sunday."
 )
 st.subheader("The Shocking Chat Chronicles !")
 st.image("screenshots/monthly.png")
 st.markdown(
    "March, my birthday month, surprisingly saw a dip in messages! Perhaps the celebrations were more in-person, leaving the digital space quieter than expected. "
    "Then came May, June, and July, the summer months away from college—where online chats with friends and work took center stage, leading to a massive surge in messages. "
    "The energy was high, with constant catching up, virtual hangouts, and project discussions. But August hit like a reset button, with messages slowing as routines settled in. "
    "As the year wrapped up, December brought a festive comeback, reviving chats with holiday greetings and year-end reflections. A year of unexpected digital twists!"
 )

 st.subheader("🕒 Night Owl")
 st.image("screenshots/hourly.png")
 st.markdown(
    "My messaging habits have two clear peaks: late at night and in the evening. "
    "The early hours of the day are silent, but as the night sets in, my chats reach their peak at **midnight**—perhaps those deep conversations and late-night memes."
 )
 
with tabs[3] :

 # Chapter 2: Response Times
 st.header("📊 Chapter 2: Priorities in Action: Chat Response Times")
 st.subheader("Some chats are rapid-fire, while others take their time...")
 st.image("screenshots/response_time1.png")
 st.image("screenshots/response_time3.png")
 st.markdown(
    """
    Some chats demand immediate attention, while others are more laid-back.<br>
    The fastest response? **Co-Coordinator**, averaging just 17 minutes—a clear sign of how crucial work-related communication is. These chats likely drive important decisions and updates. There’s no room for delays when decisions need to be made on the fly.<br><br>

    Then there’s **Arpan, Ujjwal, and Surya** – my work buddies who also happen to be close friends. These chats are all about balance. One minute, we’re deep into work discussions, and the next, we’re laughing over memes. Response time here? Around 60 minutes – fast enough to keep the conversations going without feeling rushed.<br><br>

    On the flip side, take my chats with **Nidheesh**. These are convos which are a bit relaxed and only when the situation demands. With an average response time of 1,782 minutes (yeah, that’s more than a day!), these chats are all about catching up whenever the mood strikes.
    """,
    unsafe_allow_html=True
 )
 st.subheader("Group Response Time: Work vs. Friends vs. Juniors")
 st.image("screenshots/response_time2.png")
 st.markdown(
    """
    - **Work chats** are the fastest with an average response time of **106.5 minutes**—likely because staying on top of updates and tasks is key to keeping things running smoothly.  
    - **Friend chats** average **158.5 minutes**, striking a balance between casual conversations and occasional bursts of excitement when sharing memes or planning hangouts.  
    - With **Juniors**, the response time jumps to **699.9 minutes**—often a result of spaced-out, less frequent conversations. These are more relaxed and usually happen when the need arises.
    """
 )
with tabs[4] :
 # Chapter 3: Important Chats
 st.header("🧩 Chapter 3: Chat Patterns")
 st.subheader("📊 My Contribution to Each Chat (%)")
 st.image("screenshots/chat_pattern1.png")
 st.image("screenshots/chat_pattern2.png")

 st.markdown(
    "This percentage highlights my engagement in different chats and shows where I’m most active versus where I just listen in."
 )

 # Subtopic 2: Average Message Length
 st.subheader("✍️ Average Message Length")
 st.image("screenshots/chat_pattern3.png")
 st.image("screenshots/chat_pattern4.png")
 st.markdown(
    "Am I a person of few words or do I prefer detailed conversations? This reveals the average length of each message exchanged across various chats."
 )

 # Subtopic 3: Daily Chat Activity
 st.subheader("📅 Average Messages Per Day")
 st.image("screenshots/chat_pattern5.png")
 st.image("screenshots/chat_pattern6.png")
 st.markdown(
    "Work chats dominate with **86.1** messages per day, highlighting how essential quick, consistent communication is for staying aligned on tasks and decisions. "
    "Friend chats average **58.7** messages daily, creating a balance between casual banter and deeper conversations. Meanwhile, chats with juniors average **11.3** messages per day, often for quick check-ins or advice when needed."
 )

 # Subtopic 4: Unique Days of Activity Per Chat
 st.subheader("📆 Number of Unique Active Days")
 st.image("screenshots/chat_pattern7.png")
 st.image("screenshots/chat_pattern8.png")
 st.markdown(
    "Friends take the lead with **974** unique days of chats, showing how these connections are a constant part of daily life. "
    "Whether it’s quick check-ins or long conversations, they help keep the bond alive. Work chats follow with **398** unique days, which reflects their project-based, need-driven nature—active when deadlines or updates are in play, but not necessarily every day. "
    "Chats with juniors, with **158** unique days, tend to be sporadic and situation-based, often limited to mentorship or guidance when needed."
 )

with tabs[5] :

 # Chapter 4: Word Analysis
 st.header("🎭 Chapter 4: What Do I Talk About?")
 st.subheader("The words I use the most say a lot about me!")
 st.image("screenshots/wordcloud1.png")
 st.markdown(
    "This word cloud gives an overall glimpse into the most frequently used words across all chats. "
    "Overall, the cloud shows a blend of formality and informality, highlighting how chats often shift between serious discussions and casual banter, capturing the essence of both personal and professional exchanges."
 )

 st.subheader("With Friends and Family:")
 st.image("screenshots/wordcloud2.png")
 st.markdown(
    "When I look at this word cloud of my chats with friends and family, it feels like a snapshot of my daily life. **Bhai, yaar, and haan** jump out instantly—pretty much staples in almost every conversation. "
    "Whether I’m asking **“kya kar rha?”** or responding with **“Acha, sahi hai,”** it’s all about staying connected and keeping up with what everyone’s doing. "
    "I can almost hear the playful banter and casual catch-ups in every word."
 )

 st.subheader("Work:")
 st.image("screenshots/wordcloud3.png")
 st.markdown(
    "Looking at this word cloud of my work chats, it’s clear that my life as the CP (Competitive Programming) club coordinator is pretty active! "
    "Words like **code, contest, event, and workshop** pop up a lot—showing how much work is being done on events or helping others debug code. "
    "It’s all about keeping the team in sync, solving problems on the fly, and making sure the club is running smoothly. There’s never a dull moment!"
 )

 st.subheader("Juniors:")
 st.image("screenshots/wordcloud4.png")
 st.markdown(
    "This word cloud reflects my chats with juniors, where **kya, karna, and contest** pop up frequently. "
    "There’s a lot of **bhaiya** thrown in as they frequently ask about **Codeforces and leaderboard** updates. "
    "It’s all about answering questions, sharing resources, and pushing them to sharpen their problem-solving skills. Always feels good to guide them."
 )
 navigate_to_section("Conclusion")

with tabs[6] :

 # Conclusion
 st.header("📌 Conclusion: Wrapping Up the Story")
 st.image("screenshots/correlation.png")
 st.markdown("### Key Takeaways")



 # 1. Total Messages vs. Average Messages per Day
 st.subheader("1️⃣ Daily Consistency Drives Engagement")
 st.markdown("""
 A **strong positive correlation (0.92)** shows that my total messages are directly tied to how consistently I chat daily.  
 The more I engage in everyday conversations, the higher my overall message volume.  
 **Key Insight:** Regular chats, even if short, help drive deeper engagement over time.
 """)

 # 2. Friend Chats vs. Average Message Length
 st.subheader("2️⃣ Short and Sweet with Friends")
 st.markdown("""
 There’s a **strong negative correlation (-0.72)** between friend chats and average message length.  
 Friend conversations tend to be quick, casual exchanges, rather than long discussions.  
 **Conclusion:** These chats are about frequent check-ins and sharing laughs, not lengthy talks.
 """)

 # 3. Total Messages vs. Response Time
 st.subheader("3️⃣ Speed Fuels Conversations")
 st.markdown("""
 A **moderate negative correlation (-0.55)** between total messages and response time highlights the power of quick replies.  
 Faster responses lead to more engaging, back-and-forth conversations.  
 **Takeaway:** Reducing response time helps boost overall message volume and keeps chats active.
 """)

 # 4. Friend Chats vs. Work Chats
 st.subheader("4️⃣ Work-Life Boundaries")
 st.markdown("""
 A **strong negative correlation (-0.66)** shows that friend and work chats are distinct, with little overlap.  
 When I’m focused on work, friend chats slow down, and vice versa.  
 **Insight:** Clear boundaries help balance social life and work priorities.
 """)

 # 5. Work Chats vs. Average Message Length
 st.subheader("5️⃣ Detailed Discussions in Work Chats")
 st.markdown("""
 Work chats have a **moderate positive correlation (0.48)** with average message length.  
 This indicates more thoughtful and detailed conversations, likely due to project discussions and problem-solving.  
 **Key Insight:** Work-related chats require clarity and thorough communication.
 """)

 # 6. Total Messages vs. Unique Days
 st.subheader("6️⃣ Consistent Activity Across Days")
 st.markdown("""
 A **moderate positive correlation (0.64)** between total messages and unique days suggests frequent, consistent conversations lead to more messages overall.  
 Even small daily chats can add up to significant engagement over time.  
 **Conclusion:** Daily consistency strengthens relationships and boosts overall message counts.
 """)

 # 7. Friend Chats vs. Unique Days
 st.subheader("7️⃣ Friends Are a Daily Habit")
 st.markdown("""
 Friend chats show a **strong positive correlation (0.72)** with unique days of activity, reflecting their role in daily life.  
 Whether it’s quick check-ins or extended conversations, friends are a constant in my messaging routine.  
 **Key Insight:** Strong relationships thrive on frequent interactions across multiple days.
 """)

 # 8. Average Length vs. Response Time
 st.subheader("8️⃣ Longer Replies Take Time")
 st.markdown("""
 A **moderate positive correlation (0.45)** between message length and response time suggests that more thoughtful replies take longer to craft.  
 This balance helps ensure quality communication, especially in work or mentorship settings.  
 **Insight:** Taking time for longer, detailed responses can help foster clearer and more meaningful conversations.
 """)

 # Final Thoughts
 st.header("📌 Wrapping It All Up")
 st.markdown("""
 The correlations reveal different aspects of my chat behavior—from consistency and engagement to balancing work, friendships, and thoughtful responses.  
 With these insights, I can better understand and manage my communication habits for deeper and more meaningful connections!
 """)




