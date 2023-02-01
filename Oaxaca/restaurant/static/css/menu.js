const viewMore = document.querySelectorAll('.dropdown');

viewMore.forEach(dropdown => {
    const viewInfo = dropdown.querySelector('.dish-more-info');
    const moreInfo = dropdown.querySelector('.hidden-dish-info-row');

    viewInfo.addEventListener('click', () =>{
        moreInfo.classList.toggle('show-dish-info-row');
    });
});
