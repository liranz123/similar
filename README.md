## The Problem: 

As Production Engineers we are facing a challenge of managing a growing number
website domains and due to that growing number of certificates. Maintaining those certificates
manually has become a real issue and we need a tool that will alert us when there is a 
potential issue with a certificate.

## Solution: 

Implement the function `solution`, you can use as many funciton helpers as you like.  

The function takes 3 input parameters
```python
def solution(domain, file_path, allowed_days):
    # Please write your code here.
    return ["a", "b"]

```

Given the function inputs (see inputs below) it should analyze the certificate data inside a file and 
return a report about the given domain (see outputs below).
The function should be able to handle errors and return the word "error" incase of any error.


## Inputs: 

- *Important* The `solution` function will be called automatically against pre-computed 
test cases (some are visibile under the `Test Cases` tab, e.g there is no need to call the `solution(...)` 
function by yourself it will be called automatically. 

- `domain`: Target domain name to create report from the file.
- ` file_path`: Path to file containg information about different domains.
- `allowed_days`: A number indicating the minimal valid days for a certificate to exist from 
creation time until expiration.

## Outputs: 

A Valid output be a list of strings in the following order:

[`domain_name`,` number_of_alternative_names`,` alt_name1`,` alt_name2`,...`,alt_nameN`,` total_days_certificate_valid`,` should_alert_on_days` ]

- `domain_name`: The given domain name. 
- `number_of_alternative_names`: number of all the unique alternative names (`subjectAltName` key) do not include the input domain. i.e if the given domain is foo.com ,  *www.foo.com* and *foo.com*  will count as zero..
- `alt_nameX`: **SORTED**  alphabetically for each alternative name add it to the list (length of `alt_name` should be equal to `number_of_alternative_names`) 
- ` total_days_certificate_valid`: The total days that the certificate is valid from creation until expiration.
- `should_alert_on_days`: `true` if `allowed_days` is smaller or equal to` total_days_certificate_valid`, `false` otherwise


## Example: 

Given the certificate for domain `example.com`: 

```
notBefore: Nov  3 00:00:00 2021 GMT 
notAfter: Dec  3 23:59:59 2021 GMT
subjectAltName: api.example.com, *.other-domain.com, qa.example.com, www.example.com, ok-www.example.com` 
```

### Input:

- file_path: `some path to file` 
- domain: `example.com`
- allowed_days: `60`

### Output: 

The output should be the following list: 

["example.com", "4" , "*.other-domain.com", "api.example.com", "ok-www.example.com", "qa.example.com", "30", "true"]

# Tips:

- Check the `Solutions` tab to see an example.
- You can run this code locally and test against the input file in the `Files` tab, just make sure to submit the final code here on time :) 
-  Recommended packages: `json`, `datetime`


