# Internet Speed Twitter Bot

An automated Python bot that:

* Runs an internet speed test using **Speedtest.net**
* Extracts **download** and **upload** speeds after they fully load
* *(Planned)* Logs into **X/Twitter** and tweets at your internet provider if your speeds are below the promised service level

---

## 🚀 Features

### ✔ Automated Speed Test

The bot launches Chrome with Selenium, navigates to Speedtest.net, accepts the cookie popup, clicks **Go**, and waits for real numeric results (not placeholder dashes `—`).

### ✔ Reliable Speed Extraction

Speedtest temporarily displays `—` before showing actual speeds.
To ensure accurate results, the bot uses a custom Selenium `ExpectedCondition`:

```python
class TextNotEmpty:
    ...
```

This waits until the download/upload values contain **real numbers**, not placeholders.

### ✔ Ready for Twitter Automation

The structure includes a `tweet_at_provider()` function, ready for future automation such as:

* Logging into X/Twitter
* Composing a tweet
* Tagging your ISP with actual speeds

---

## 🧩 How It Works

### 1. Initialize the Bot

```python
bot = InternetSpeedTwitterBot()
```

This starts a Chrome browser using Selenium.

---

### 2. Run the Speed Test

```python
bot.get_internet_speed()
```

The method:

* Opens Speedtest.net
* Accepts cookies (if present)
* Clicks the **Go** button
* Waits for Speedtest to produce actual results
* Stores them in:

```python
bot.down
bot.up
```

---

## 📌 Example Output

```
Download speed: 128.45
Upload speed: 9.87
```

---

## 🛠 Requirements

* Python 3.9+
* Google Chrome installed
* Selenium:

```bash
pip install selenium
```

ChromeDriver is auto-managed by Selenium 4.6+.

---

## 📁 Project Structure

```
internet_speed_twitter_bot/
│
├── twitter_bot.py        # Main bot logic
└── README.md             # Project documentation
```

---

## 📌 Next Steps (Planned)

* Automate login to X/Twitter
* Automatically post a tweet tagging your ISP
* Add environment variable support for login credentials
* Add speed thresholds to trigger tweeting only when required

---

## ⭐ Contributing

Pull requests and improvements are welcome!
Feel free to open issues for suggestions or bug reports.

