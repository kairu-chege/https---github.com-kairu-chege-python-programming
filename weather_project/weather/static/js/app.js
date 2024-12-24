$(document).ready(function() {
  // Event listener for the search button
  $('#search-button').click(function() {
    const city = $('#city-search').val(); // Get the city name from the input
    $('#loading').show(); // Show loading animation
    $('.weather-details').hide(); // Hide weather details initially

    // Asynchronous AJAX request using promises
    axios.defaults.xsrfHeaderName = "X-CSRFToken";
    axios.defaults.xsrfCookieName = "csrftoken";
    axios.post('/', {
      city: city,
      csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val() // Include CSRF token
    })
    .then(response => {
      console.log(response.data);
      const data = response.data;
      console.log(data.name); // Check if city name is present
      console.log(data.main.temp); // Check if temperature is present
      $('#loading').hide(); // Hide loading animation after successful response
      $('.city').text(data.name); // Update city name
      $('.temp').text(data.main.temp + '°C'); // Update temperature
      $('.humidity').text('Humidity: ' + data.main.humidity + '%'); // Update humidity
      $('.wind').text('Wind Speed: ' + data.wind.speed + ' m/s'); // Update wind speed
      $('.pressure').text('Pressure: ' + data.main.pressure + ' hPa'); // Update pressure
      $('.description').text(data.weather[0].description); // Update weather description
      $('.weather-icon').attr('src', 'http://openweathermap.org/img/wn/' + data.weather[0].icon + '@2x.png'); // Update weather icon
      $('.weather-details').show(); // Show weather details
    })
    .catch(error => {
      $('#loading').hide(); // Hide loading animation even on error
      alert('Error: ' + error.message); // Show a more informative error message
    });
  });
});