//Fetches the class dropdown which will be used to loop through to find every definition under it
const viewMore = document.querySelectorAll('.dish-info-dropdown');

viewMore.forEach(dropdown => {
    //Assigned the information to be shown as moreInfo
    const moreInfo = dropdown.querySelector('.dish-info-row');
    //Assigned the text of the button as button
    const button = dropdown.querySelector('.dish-info-dropdown-btn')

    //Created a functionality that understands whenever the dropdown button is pressed
    button.addEventListener('click', () => {
        button.classList.toggle("view-less");
        moreInfo.classList.toggle("show");
    });
});

// Highlight menu category on scroll
const menuCategories = document.querySelectorAll('.dish-cards-category');
const categoryNav = document.querySelectorAll('.menu-category');
const menuList = document.querySelector('#menu-list');
const SCROLL_PADDING_TOP = 65;
const SCROLL_MARGIN_ERROR = 15;
window.onscroll = () => {
    var current = "";

    menuCategories.forEach((category) => {
        if (window.pageYOffset >= (category.offsetTop - SCROLL_PADDING_TOP)) {
            current = category.getAttribute("id");
        }

    });

    categoryNav.forEach((a) => {
        a.classList.remove("active");
        if (window.pageYOffset > (menuList.offsetTop - SCROLL_PADDING_TOP + SCROLL_MARGIN_ERROR) && a.innerText.includes(current)) {
            a.classList.add("active");
        }
    });
};

// Toggle show/hide for collapsible headings
const collapsibleHeadings = document.querySelectorAll('.heading-collapsible');
collapsibleHeadings.forEach(heading => {
    let content = heading.nextElementSibling;
    if (content) {
        heading.addEventListener('click', () => {
            heading.classList.toggle("active");
            if (content.style.maxHeight) {
                content.style.maxHeight = null;
            } else {
                content.style.maxHeight = content.scrollHeight + "px";
            }

        });
    }
})

// Functionality for each dish card (-) and (+) buttons
const dishOrderSubBtns = document.querySelectorAll('.dish-count-sub');
const dishOrderAddBtns = document.querySelectorAll('.dish-count-add');
const MIN_ORDER_COUNT = 1;
const MAX_ORDER_COUNT = 10;
dishOrderSubBtns.forEach(subBtn => {
    let dishCountInput = subBtn.nextElementSibling;
    if (dishCountInput) {
        subBtn.addEventListener('click', () => {
            if (dishCountInput.value > MIN_ORDER_COUNT) {
                dishCountInput.value = parseInt(dishCountInput.value) - 1;
            }
        });
    }
});
dishOrderAddBtns.forEach(addBtn => {
    let dishCountInput = addBtn.previousElementSibling;
    if (dishCountInput) {
        addBtn.addEventListener('click', () => {
            if (dishCountInput.value < MAX_ORDER_COUNT) {
                dishCountInput.value = parseInt(dishCountInput.value) + 1;
            }
        });
    }
});

// Function for filtering menu items in menu
function filterMenu(filters) {
    resetDishCards(); // show all dishes before filtering

    let dishAllergensElement = document.querySelector('#dish-allergens');
    if (!dishAllergensElement) {
        console.log("Allergen information missing.")
        return;
    }
    const dishAllergens = JSON.parse(dishAllergensElement.textContent);
    dishesToHide = []; // list of dish ids to hide
    filters.forEach(filter => {
        dishAllergens.forEach(dish => {
            if (dish.dish_allergen_list.includes(filter)) dishesToHide.push(dish.dish_id);
        })
    })

    hideDishCards(dishesToHide); // hide dishes with ids
}

function resetDishCards() {
    const dishCards = document.querySelectorAll('.dish-card');
    if (dishCards) {
        dishCards.forEach(card => card.classList.remove('hidden'));
    }
}

function hideDishCards(dishes) {
    dishes.forEach(dish => {
        dishCards = document.querySelectorAll((".dish-" + dish));
        dishCards.forEach(card => hideDish(card));
    });
}

function hideDish(card) {
    card.classList.add('hidden');
}

//
function filterMenuGetChecked() {
    const filterToggles = document.querySelectorAll('.slide-toggle-checkbox');
    return Array.from(filterToggles)
        .filter(toggle => toggle.checked) // select only checked toggles
        .map(toggle => toggle = toggle.value); // get filter value of checked toggles
}

// Function for filtering menu items with filter checkboxes
function filterMenuCheckbox() {
    filterMenu(filterMenuGetChecked());
}

// Function for fitering menu items with search
function filterMenuSearch(query) {

}

// Checking if enter key is pressed in the search bar to start filtering.
const searchInput = document.querySelector('#Search')
searchInput.addEventListener('keypress', function(e) {
    if(e.key === 'Enter'){
        e.preventDefault();
        const term = searchInput.value.toLowerCase();
    }
});

//function for filtering with the search term
function searchFilter(term){

}
