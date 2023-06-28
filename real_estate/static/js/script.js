document.addEventListener('DOMContentLoaded', () => {
    // Fetch the news data from the server
    fetch('/news/')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not OK');
        }
        return response.json(); // Parse the response as JSON
      })
      .then(data => {
        console.log('Received data:', data); // Add this line for debugging
  
        // Get the news container element
        const newsContainer = document.getElementById('news');
  
        // Iterate over each news item
        data.forEach(newsItem => {
          // Create the news item element
          const newsItemElement = document.createElement('div');
          newsItemElement.classList.add('news-item');
  
          // Create the title element
          const titleElement = document.createElement('h3');
          titleElement.textContent = newsItem.title;
  
          // Create the description element
          const descriptionElement = document.createElement('p');
          descriptionElement.textContent = newsItem.description;
  
          // Create the URL element
          const urlElement = document.createElement('a');
          urlElement.href = newsItem.url;
          urlElement.target = '_blank';
          urlElement.textContent = 'Read';
  
          // Append the title, description, and URL elements to the news item element
          newsItemElement.appendChild(titleElement);
          newsItemElement.appendChild(descriptionElement);
          newsItemElement.appendChild(urlElement);
  
          // Append the news item element to the news container
          newsContainer.appendChild(newsItemElement);
        });
      })
      .catch(error => console.error(error));
  });
  