
## 💡 What's Inside?
- A **Block** class to represent each block
- A **Blockchain** class to manage the full chain
- The first block is a **Genesis block**
- New blocks can be added easily with data

## 🧱 Each block has:
- Index (block number)
- Timestamp (when it was made)
- Data (anything you want to store)
- Hash of the previous block
- Its own hash (made using SHA256)

## ✅ Validating the chain
The chain checks if:
- The current block's hash matches the data
- Each block is connected properly to the previous one

## 🛠️ How to Run
```bash
python blockchain.py
