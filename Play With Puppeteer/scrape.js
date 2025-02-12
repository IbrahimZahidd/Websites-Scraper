const fs = require("fs");
const puppeteer = require("puppeteer");
async function autoScroll(page, maxScrolls) {
  await page.evaluate(async (maxScrolls) => {
    await new Promise((resolve) => {
      var totalHeight = 0;
      var lastScrollHeight = document.body.scrollHeight; // store initial scroll height
      var distance = 500;
      var scrolls = 0; // scrolls counter
      var resetCounter = 0; // counter to reset scrolls if scroll height changes
      var timer = setInterval(() => {
        var scrollHeight = document.body.scrollHeight;
        window.scrollBy(0, distance);
        totalHeight += distance;
        scrolls++; // increment counter

        // reset scrolls if scroll height changes
        if (scrollHeight !== lastScrollHeight) {
          resetCounter++;
          if (resetCounter >= 5) {
            // if scroll height changes continuously for 5 times, reset scrolls
            scrolls = 0;
            totalHeight = 0;
            resetCounter = 0;
          }
        } else {
          resetCounter = 0; // reset counter if scroll height doesn't change
        }

        // stop scrolling if reached the end or the maximum number of scrolls
        if (
          totalHeight >= scrollHeight - window.innerHeight ||
          scrolls >= maxScrolls
        ) {
          clearInterval(timer);
          resolve();
        }
        lastScrollHeight = scrollHeight; // update last scroll height
      }, 300);
    });
  }, maxScrolls); // pass maxScrolls to the function
}

async function scrapeFbAdsLibrary() {
  const prompts = [
    "What is the meaning of life?",
    "Explain quantum mechanics in simple terms.",
    "Write a poem about autumn.",
    "What are the benefits of meditation?",
    "Tell me a fun fact about space.",
  ];
  const randomPrompt = prompts[Math.floor(Math.random() * prompts.length)];
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();
  await page.setViewport({
    width: 1200,
    height: 800,
  });

  // navigate to the url
  await page.goto("https://chatgpt.com");
  await page.waitForNetworkIdle();
  await page.waitForSelector("textarea"); // Adjust the selector if necessary
  await page.type("textarea", randomPrompt);
  await page.waitForSelector('[data-testid="send-button"]');

  // Wait for the response to load
  await page.waitForSelector(".response-selector"); // Adjust to the actual selector for responses

  // Get the response text
  const response = await page.$eval(".response-selector", (el) => el.innerText); // Adjust to the actual selector

  // Save the response to a text file
  fs.writeFileSync(
    "response.txt",
    `Prompt: ${randomPrompt}\nResponse: ${response}`
  );

  await browser.close();
  console.log("Done!");
}

async function main() {
  await scrapeFbAdsLibrary();
}

if (require.main === module) {
  main();
}
