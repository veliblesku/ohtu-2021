*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  jore
    Set Password  jore123
    Submit Credentials
    Register Should Succeed

# Register With Too Short Username And Valid Password
# # ...

# Register With Valid Username And Too Short Password
# # ...

# Register With Nonmatching Password And Password Confirmation
# # ...

*** Keywords ***
Register Should Succeed
    Main Page Should Be Open

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open