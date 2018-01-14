$(() => {
  $.getJSON('https://swapi.co/api/films/?format=json', (js) => {
    let movies = $('ul#list_movies');
    $.each(js.results, (i, v) => {
      movies.append('<li>' + v.title + '</li>');
    });
  });
});
