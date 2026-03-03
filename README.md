# Lab-4
Using Web APIs
main.py handles user interaction and logic
dog_api.py handles all API requests and JSON parsing

API Endpoints
List all breeds:    `GET https://dog.ceo/api/breeds/list/all`

Random dog image  
   `GET https://dog.ceo/api/breeds/image/random`

Random image by breed  
   `GET https://dog.ceo/api/breed/{breed}/images/random`



## Issues

### Issue 1: API returned 404 error

**Problem:** entering an invalid breed caused a crash
**Cause:** the program did not validate user input
**Fix:** added breed validation before calling the API
**Commit:** added breed validation logic

