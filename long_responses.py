import random
R_HEALTHCARE="The Centralized Healthcare System is an online platform that allows users to view ratings and reviews of doctors and healthcare centers. Registered patients can access their medical records, rate and review doctors, while doctors can update their patients medical records and view their own ratings and reviews."
R_ACCESSRATINGS=" Any user, whether registered or not, can access the ratings and reviews of doctors and healthcare centers on our website. Simply browse the platform and explore the various profiles to find the information you need."
R_REGISTER=" To register, click on the Sing in button on the websites homepage and follow the instructions to create your account. You will need to provide some personal information."
R_VIEWRECORDS=" Yes, registered patients have access to their own medical records. Once logged in, navigate to the Medical Records section to view your medical history, test results, and other relevant information."
R_RATEREVIEW="Yes, registered patients can rate and review doctors based on their personal experiences. After logging in, visit the doctors profile page and follow the instructions to leave your rating and review."
R_SECURE="We take the security and privacy of your personal information seriously. Our platform employs robust security measures to protect your data, and we adhere to strict privacy guidelines to ensure confidentiality."
R_SUPPORT="If you have any questions, concerns, or technical issues, please visit the Contact Us page on our website. You can reach out to our customer support team, and they will be happy to assist you."
def unknown():
    response = ['could you please rephrase that?',
                "I'm not equiped to answer this,Please contact us on our contact us page",
                "What does that mean"][random.randrange(4)]
    return response