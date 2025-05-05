import streamlit as st
import time

# Title of the app
st.title("🎉 Happy Birthday My Girl! 🎂🎈")
st.balloons()

# Custom background image CSS (replace with your image URL)
background_image = """
    <style>
        body {
            background-image: url('https://www.w3schools.com/w3images/fjords.jpg');  # Example background image
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
    </style>
"""

# Render the custom background image CSS
st.markdown(background_image, unsafe_allow_html=True)

# Centered button with more attractive style
button_clicked = st.button("💌 Read More...", key="read_message")

# Emotional Birthday Message
birthday_message = """
 💌 Birthday Message for my First College Friend – Heartfelt Edition 🌸

Happy Birthday, Anu! 🎉💖✨

You were the first friend I made in college — and that will always mean something special to me. From awkward first hellos 👋 to becoming van mates 🚐, bench buddies 🛋, and partners in crime for every little thing... you’ve been by my side through it all. 🙏

You made college feel like home 🏡. You made even the dullest days feel lighter ☀️. And without even trying, you made me feel seen, heard, and understood. 🥰

I know life can feel confusing at times 🤔 — full of questions, worries, and "what ifs" — but I need you to remember something: you’re stronger 💪 than you think, wiser 🦉 than you know, and so incredibly deserving of love 💝, peace ☮️, and every beautiful thing this life has to offer. 🌺

Don’t stress too much 😌. Go with the flow 🌊. Trust the universe 🌌 — it has your back 🙌. Let time do its magic ⏳, and in the meantime, focus on your dreams 🌟. You’ve got so much potential 🔥.

And hey — never forget this girl right here, okay? 😘 I’ll always be around to laugh with you 😹, cry with you 😢, and make you laugh so hard your stomach hurts 😂 (and maybe your cheeks too 😝).

I’m wishing you everything good in life — a career you love 💼, a future that feels right 🔮, and a partner who treats your heart like gold 💛.

And I’m so, so lucky 🍀 to know you.

With all my heart,  
raahina.... 🤍💌
"""

# Custom CSS for the button and toast message
toast_html = """
    <style>
        .toast {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: #ffeb3b;
            padding: 30px;
            font-size: 24px;
            font-weight: bold;
            border-radius: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            color: #000;
            text-align: center;
        }
        .button-center {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 50px;
        }
        .btn {
            padding: 15px 30px;
            background-color: #ff6347;
            color: white;
            font-size: 20px;
            font-weight: bold;
            border-radius: 50px;
            border: none;
            cursor: pointer;
        }
        .btn:hover {
            background-color: #ff4500;
        }
    </style>
"""

# Render the custom CSS for the button and toast message
st.markdown(toast_html, unsafe_allow_html=True)

# Create a placeholder for the toast message
toast_placeholder = st.empty()

# Wait 3 seconds before removing the toast message
time.sleep(3)  # Keep the toast visible for 3 seconds
toast_placeholder.empty()  # Remove the toast message after 3 seconds

# Display the birthday message when the button is clicked
if button_clicked:
    st.write(birthday_message)

# Trigger the balloon pop-up
st.balloons()
