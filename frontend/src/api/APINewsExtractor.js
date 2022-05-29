const MakeNewsExtractorRequest = () => {
  fetch("api/news")
    .then((response) => response.json())
    .then((data) => console.log(data));
};

export { MakeNewsExtractorRequest };
