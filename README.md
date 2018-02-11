# steempass
steemit password encode and decode

- python 2.7 tested

## Usage
### encoding password
Run command below.
```bash
python enc.py
```
Input master key and steemit password then encrypted password is displayed.

```bash
master key: yourmasterkey
password to encrypt: [your steemit password]

encrypted password:
gAAAAABagBeI1x2UoGuZ7NEpUW6oby73cidTV8y4rwXN0CpGO6IdEuZFldSgQ0jT651XWZc8zOXfyuEj1hzYp0EaJhkfN8VxwMWvgLcasj5HLij6ATTDMjU=
```

`Save encrypted password to somewhere.`

### decoding password
Run command below.
```bash
python dec.py
```
Input master key and previously encrypted steemit password then decrypted password is displayed.

```bash
master key: yourmasterkey
password to decrypt: gAAAAABagBeI1x2UoGuZ7NEpUW6oby73cidTV8y4rwXN0CpGO6IdEuZFldSgQ0jT651XWZc8zOXfyuEj1hzYp0EaJhkfN8VxwMWvgLcasj5HLij6ATTDMjU=

Original password:
[your steemit password]
```
