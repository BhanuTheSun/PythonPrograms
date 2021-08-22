*** Settings ***
Documentation     It is test project


*** variables ***
${number}   10

*** Test Cases ***
My First Test Case
   Should Be Equal    ${number}     10
   
Second Test Case
   Should Not Be Equal    ${number}    11
   


*** keywords ***
