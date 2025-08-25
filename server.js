const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');

const TELEGRAM_TOKEN = 'YOUR_BOT_TOKEN';
const TELEGRAM_API = `https://api.telegram.org/bot${TELEGRAM_TOKEN}/sendMessage`;

const app = express();
app.use(bodyParser.json());

app.post('/webhook', async (req, res) => {
  const message = req.body.message;
  const chatId = message.chat.id;
  const text = message.text.trim();

  let reply = '';

  switch (text) {
    case '/start':
      reply = `Welcome! 🙌 Choose an option:\n1. 🙏 Submit a Prayer Request\n2. 👥 Join the Prayer Group`;
      break;
    case '1':
      reply = 'Please type your prayer request 🙏';
      break;
    case '2':
      reply = 'You’ve been added to the prayer group! 🎉';
      break;
    default:
      reply = 'Thank you! Your message has been received. 💌';
      // Here you could save the message to a database
  }

  await axios.post(TELEGRAM_API, {
    chat_id: chatId,
    text: reply
  });

  res.sendStatus(200);
});

app.get('/', (req, res) => {
  res.send('Telegram Prayer Bot is running 🙏');
});

app.listen(3000, () => console.log('Bot server running on port 3000'));
