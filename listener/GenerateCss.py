class GenerateCss:
    def __init__(self):
        self.code_stack = []

    def generate_code(self):
        self.code_start()

        result = ""
        for code in self.code_stack:
            result += code

        return result

    def code_start(self):
        self.generate_body()
        self.generate_container()
        self.generate_header()
        self.generate_base_info()
        self.generate_h2()
        self.generate_profile()
        self.generate_background()
        self.generate_general()
        self.generate_snackbar()
        self.generate_go_top()
        self.generate_change_theme()
        self.generate_collapsable()

    def generate_body(self):
        temp_code = """
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

body {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    margin: 0;
    padding: 0;
    color: #333;
}
"""
        self.code_stack.append(temp_code)

    def generate_container(self):
        temp_code = """
.container {
    background-color: transparent;
    width: 85%;
    max-width: 1200px;
    min-height: 100vh;
    height: fit-content !important;
    margin: 3rem auto;
    display: flex;
    flex-direction: column;
    box-shadow: 0 20px 40px rgba(0,0,0,0.15);
    border-radius: 12px;
}

.container a:hover {
    color: skyblue;
}
"""
        self.code_stack.append(temp_code)

    def generate_header(self):
        temp_code = """
/* The .information class is crucial here for the 2-column layout */
.information {
    width: 100%;
    display: flex;
    flex-direction: row;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
}
"""
        self.code_stack.append(temp_code)

    def generate_base_info(self):
        temp_code = """
.base-info {
    width: 33%;
    padding: 2.5rem;
    box-sizing: border-box;
    background-color: #0B192C; 
    color: #E2E8F0;
    display: flex;
    flex-direction: column;
    gap: 2rem;
}

.base-item {
    padding-bottom: 8px;
    border-bottom: 1px solid rgba(255,255,255,0.15);
    margin-bottom: 15px;
    text-transform: uppercase;
    font-size: 1.1rem;
    letter-spacing: 1px;
}

.base-info ul {
    list-style-type: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.base-info li {
    font-size: 0.95rem;
}

.base-info strong {
    color: #94a3b8;
    margin-right: 5px;
}
"""
        self.code_stack.append(temp_code)

    def generate_h2(self):
        temp_code = """
h2 {
    margin: 0;
    font-size: 1.4rem;
    font-weight: 600;
    color: inherit;
}
"""
        self.code_stack.append(temp_code)

    def generate_profile(self):
        temp_code = """
.profile-img {
    display: flex;
    justify-content: center;
    align-items: center;
    padding-bottom: 10px;
}

.profile-img img {
    height: 13rem;
    width: 13rem;
    border-radius: 50%;
    object-fit: cover;
    border: 5px solid rgba(255,255,255,0.1);
    box-shadow: 0 8px 16px rgba(0,0,0,0.2);
}
"""
        self.code_stack.append(temp_code)

    def generate_background(self):
        temp_code = """
.background {
    display: flex;
    justify-content: center;
    margin: 0;
    background-attachment: fixed;
}
"""
        self.code_stack.append(temp_code)

    def generate_general(self):
        temp_code = """
.additional-info {
    width: 67%;
    padding: 3.5rem;
    box-sizing: border-box;
    background-color: #ffffff;
    display: flex;
    flex-direction: column;
    gap: 2.5rem;
}

/* Themes setup */
.t1 .base-info { background-color: #141E46; color: white; }
.t2 .base-info { background-color: #2B2A4C; color: white; }
.t3 .base-info { background-color: #454545; color: white; }

/* رنگ کرمی (#FFF5E0) را به سفید استخوانی (#F9F6EE) یا سفید خالص (#ffffff) تغییر دادیم */
.t1 .additional-info { background-color: #F9F6EE; color: #333; } 
.t2 .additional-info { background-color: #EEE2DE; color: #333; }
.t3 .additional-info { background-color: #FFE6C7; color: #333; }

.info-item {
    display: flex;
    flex-direction: column;
    gap: 1.2rem;
}

.additional-info-title {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    gap: 15px;
    border-bottom: 2px solid #f1f5f9;
    padding-bottom: 10px;
}

.additioan-info-titles-icon {
    width: 28px;
    opacity: 0.7;
}

/* Skills Formatting */
.additional-info-list {
    display: grid;
    grid-template-columns: 1fr 1fr;
    row-gap: 1.5rem;
    column-gap: 3rem;
    padding: 0;
    margin: 0;
    list-style-type: none;
}

.additional-info-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
}

.skill-name {
    font-weight: 500;
    font-size: 1rem;
    display: flex;
    align-items: center;
}

.skill-name::before {
    content: "•";
    color: #0B192C;
    font-size: 1.5rem;
    margin-right: 10px;
    line-height: 1;
}

.rate {
    display: flex;
    gap: 4px;
}

.rate-star {
    width: 16px;
    opacity: 0.9;
}

/* Projects & Experience */
.projects, .educations {
    display: flex;
    gap: 2rem;
    flex-direction: column;
    padding-left: 0;
    list-style: none;
}

.projects div, .educations div {
    display: flex;
    flex-direction: column;
    gap: 8px;
    position: relative;
    padding-left: 20px;
    border-left: 3px solid #e2e8f0;
}

/* Typography & Links */
.link-white {
    text-decoration: none;
    color: #e2e8f0;
    transition: color 0.3s;
    font-size: 0.95rem;
}

.link-white:hover {
    color: #fff;
    text-decoration: underline;
}

.link {
    text-decoration: none;
    color: #0B192C;
    font-weight: 600;
    font-size: 1.15rem;
}

.link:hover {
    color: #3b82f6;
}

.text {
    font-weight: 400;
    color: #64748b;
    margin: 0;
    line-height: 1.7;
    text-align: justify;
}

hr.rounded {
    display: none;
}

.info-title {
    display: flex;
    justify-content: flex-start;
    align-items: center;
    gap: 10px;
}

.base-info-icon {
    width: 30px;
}
"""
        self.code_stack.append(temp_code)

    def generate_snackbar(self):
        temp_code = """
/* snack bar */
#email-snackbar , #phone-snackbar {
    visibility: hidden;
    min-width: 250px;
    margin-left: -125px;
    background-color: #333;
    color: #fff;
    text-align: center;
    border-radius: 2px;
    padding: 16px;
    position: fixed;
    z-index: 100;
    left: 50%;
    bottom: 30px;
    border-radius: 3rem;
    font-size: 1rem;
}

#email-snackbar.show  , #phone-snackbar.show{
    visibility: visible;
    -webkit-animation: fadein 0.5s, fadeout 0.5s 2.5s;
    animation: fadein 0.5s, fadeout 0.5s 2.5s;
}

@-webkit-keyframes fadein {
    from {bottom: 0; opacity: 0;}
    to {bottom: 30px; opacity: 1;}
}

@keyframes fadein {
    from {bottom: 0; opacity: 0;}
    to {bottom: 30px; opacity: 1;}
}

@-webkit-keyframes fadeout {
    from {bottom: 30px; opacity: 1;}
    to {bottom: 0; opacity: 0;}
}

@keyframes fadeout {
    from {bottom: 30px; opacity: 1;}
    to {bottom: 0; opacity: 0;}
}
"""
        self.code_stack.append(temp_code)

    def generate_go_top(self):
        temp_code = """
/* go top btn */
.go-top{
    background-color: #0B192C;
    position: fixed;
    bottom: 16px;
    right: 32px;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    color: #fff;
    text-decoration: none;
    opacity: 0;
    pointer-events: none;
    transition: all .4s;
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
}

.go-top.active{
    bottom: 32px;
    pointer-events: auto;
    opacity: 1;
}
"""
        self.code_stack.append(temp_code)

    def generate_change_theme(self):
        temp_code = """
.change-theme-btn {
    padding: 10px 15px;
    margin: 5px 0;
    border: none;
    border-radius: 5px;
    font-size: 14px;
    font-weight: bold;
    cursor: pointer;
    transition: transform 0.2s ease;
    display: block;
}

.change-theme-btn:hover {
    transform: scale(1.05);
}

.button-container {
    position: fixed;
    top: 20px;
    left: 20px;
    display: flex;
    flex-direction: column;
    color: white;
    z-index: 100;
}

.button-container button:nth-child(1) {
    background-color: #FFF5E0;
    color: #141E46;
}

.button-container button:nth-child(2) {
    background-color: #EEE2DE;
    color: #2B2A4C;
}

.button-container button:nth-child(3) {
    background-color: #FFE6C7;
    color: #454545;
}
"""
        self.code_stack.append(temp_code)

    def generate_collapsable(self):
        temp_code = """
.collapsable {
    cursor: pointer;
    transition: opacity 0.3s;
}

.collapsable:hover {
    opacity: 0.7;
}
"""
        self.code_stack.append(temp_code)