//Fetches the class dropdown which will be used to loop through to find every definition under it
const viewMore = document.querySelectorAll('.dropdown');

viewMore.forEach(dropdown => {
    //Assigned the dropdown button as viewInfo
    const viewInfo = dropdown.querySelector('.dish-more-info');
    //Assigned the information to be shown as moreInfo
    const moreInfo = dropdown.querySelector('.hidden-dish-info-row');
    //Assigned the text of the button as button
    const button = dropdown.querySelector('.view-more')

    moreInfo.style.display = "none";

    //Created a functionality that understands whenever the dropdown button is pressed
    viewInfo.addEventListener('click', () =>{
        //Conditional statement checking if the information should be shown or hidden
        if (moreInfo.style.display === "none"){
            moreInfo.style.display = "block";
            moreInfo.style.opacity = "1";
            button.textContent = "View Less";
        } else {
            moreInfo.style.display = "none";
            moreInfo.style.opacity = "0";
            button.textContent = "View More";
        }
    });
});


// Function for filtering menu items in menu
function filterMenu() {
    console.log("filter")
}

//
function filterMenuGetChecked() {

}

// Function for filtering menu items with filter checkboxes
function filterMenuCheckbox() {

}

// Function for fitering menu items with search
function filterMenuSearch(query) {

}