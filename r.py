import os
import streamlit as st

# Set up page configuration
st.set_page_config(page_title="A Quick Note", page_icon="✉️", layout="centered")

# File where messages will be saved
MESSAGES_FILE = "messages.txt"

# Initialize session state to track page navigation
if "page" not in st.session_state:
    st.session_state.page = "welcome"
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# --- HIDDEN ADMIN ROUTE ---
# If you type ?admin=true at the end of your URL, you can see her messages.
# Example: https://your-app.streamlit.app/?admin=true
query_params = st.query_params
if "admin" in query_params and query_params["admin"] == "true":
    st.title("📬 Received Messages")
    
    password = st.text_input("Enter Admin Password", type="password")
    # CHANGE THIS PASSWORD TO WHATEVER YOU WANT
    if password == "mysecret123": 
        if os.path.exists(MESSAGES_FILE):
            with open(MESSAGES_FILE, "r", encoding="utf-8") as f:
                messages = f.read().split("--- NEW MESSAGE ---")
            
            for msg in reversed(messages):
                if msg.strip():
                    st.text_area("Message Detail", value=msg.strip(), height=100, disabled=True)
        else:
            st.info("No messages received yet.")
    elif password:
        st.error("Incorrect password.")
    st.stop()  # Stop rendering the rest of the user-facing app if in admin mode


# --- PAGE 1: THE WELCOME ---
if st.session_state.page == "welcome":
    st.title("Hi Reshika 👋")
    st.write(
        "I wanted to share a quick, respectful note with you to clear the air, "
        "without putting you on the spot or forcing an awkward conversation."
    )
    st.write("Do you have a brief moment to read it?")
    
    if st.button("Yes, continue"):
        st.session_state.page = "note"
        st.rerun()

# --- PAGE 2: THE NOTE & LOCAL MESSAGE FIELD ---
elif st.session_state.page == "note":
    st.title("Just wanted to say...")
    
    # --- MUSIC EMBED ---
    st.write("🎵 *A song to listen to while reading, if you'd like:*")
    st.video("https://www.youtube.com/watch?v=KHLVe7F7BKU") 
    
    st.markdown("---")
    
    st.info(
        "Thank you for being direct with me the other day. I truly respect your honesty, "
        "and I think loyalty is a rare and wonderful trait."
    )
    
    st.write(
        "My intentions were purely just because I think you're a great person. "
        "There is absolutely no pressure here, "
        "I am completely stepping back to respect your "
        "relationship and your boundaries."
    )
    
    st.write(
        "If you ever happen to need a helping hand with anything down the line, "
        "you know where to find me. Otherwise, I genuinely wish you nothing but "
        "continuous happiness, peace, and prosperity in everything you do."
    )
    
    st.markdown("---")
    
    # --- INTERNAL MESSAGE BOX ---
    st.subheader("Leave a message (Optional)")
    
    if not st.session_state.submitted:
        st.write("If you'd like to say anything back, you can leave a note below. It goes straight to me.")
        user_message = st.text_area("Type your message here...", height=120, label_visibility="collapsed")
        
        if st.button("Send Message"):
            if user_message.strip():
                # Append message locally to the text file
                with open(MESSAGES_FILE, "a", encoding="utf-8") as f:
                    f.write(f"\n--- NEW MESSAGE ---\n{user_message.strip()}\n")
                
                st.session_state.submitted = True
                st.rerun()
            else:
                st.warning("Please type a message before clicking send.")
    else:
        st.success("Thank you! Your message has been saved privately.")
    
    st.markdown("---")
    st.markdown("<p style='text-align: center; color: gray;'>Take care,<br><b>Asit 'Dexter' Pradhan</b> ✨</p>", unsafe_allow_html=True)