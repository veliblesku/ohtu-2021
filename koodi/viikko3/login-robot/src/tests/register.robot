*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  jani  salasanajani123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle444
    Output Should Contain  Username already taken

Register With Too Short Username And Valid Password
    Input Credentials  as  asdddd123
    Output Should Contain  Username too short and must contain characters a-z

Register With Valid Username And Too Short Password
    Input Credentials  jani  as
    Output Should Contain  Password too short and can't contain only numbers

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  jani  morojape
    Output Should Contain  Password too short and can't contain only numbers

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command