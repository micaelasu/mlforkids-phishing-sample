from checks import (
    checkAddressType, checkUrlLength, checkShortening, 
    checkAtSign, checkPortNumber, checkDomainAge, 
    checkRedirects, checkDomainRegistration
)
from miforkidsnumbers import MLforkidsNumbers

# PASTE YOUR PROJECT DETAILS HERE (from ML for Kids website)
project = "YOUR_PROJECT_ID"  # ← Replace with your project ID
model = "YOUR_MODEL_NAME"    # ← Replace with your model name

def checkUrl(addr):
    address_type = checkAddressType(addr)
    url_length = checkUrlLength(addr)
    shortening = checkShortening(addr)
    includes_at = checkAtSign(addr)
    port_number = checkPortNumber(addr)
    domain_age = checkDomainAge(addr)
    redirects = checkRedirects(addr)
    domain_reg = checkDomainRegistration(addr)

    print("URL:", addr)
    print("Address type:", address_type)
    print("URL length:", url_length)
    print("Shortening service:", shortening)
    print("Includes @:", includes_at)
    print("Port number:", port_number)
    print("Domain age:", domain_age)
    print("Redirects:", redirects)
    print("Domain registration:", domain_reg)

    # Classify using ML for Kids
    ml = MLforkidsNumbers(project, model)
    prediction = ml.classify({
        "address_type": address_type,
        "url_length": url_length,
        "shortening": shortening,
        "includes_at": includes_at,
        "port_number": port_number,
        "domain_age": domain_age,
        "redirects": redirects,
        "domain_reg": domain_reg
    })

    print("Prediction:", prediction["class_name"])
    print("Confidence:", prediction["confidence"], "%\n")

# Test URLs
checkUrl("https://www.bbc.com")  # Safe example
checkUrl("http://paypal@phishing.com/login")  # Phishing example
