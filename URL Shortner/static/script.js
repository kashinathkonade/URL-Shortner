function shortenUrl() {
  const longUrlInput = document.getElementById('longUrl');
  const resultDiv = document.getElementById('result');

  const longUrl = longUrlInput.value;

  fetch('/shorten', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: `longUrl=${encodeURIComponent(longUrl)}`,
  })
  .then(response => response.json())
  .then(data => {
    resultDiv.innerHTML = `Shortened URL: <a href="${data.shortUrl}" target="_blank">${data.shortUrl}</a>`;
  })
  .catch(error => {
    console.error('Error:', error);
    resultDiv.innerHTML = 'Error shortening URL';
  });
}
