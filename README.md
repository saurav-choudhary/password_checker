# password_checker

NOTE: The program takes the first five characters of the hashed password(s) and sents an API request to the server to fetch all the matching hashes and then compares it to the entire hash locally on the machine which makes it much more secure.

```bash
python3 checkmypass.py {password(s)}
```
