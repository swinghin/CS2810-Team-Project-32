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

const dishAddCartBtns = document.querySelectorAll('.dish-add-btn');
dishAddCartBtns.forEach(addCartBtn => {
    addCartBtn.addEventListener('click', () => {
        addToCart(addCartBtn.closest('.dish-card'))
    });
})

let newcart = {};
cartLoad();
cartView();

function addToCart(dishDiv) {
    // Get dish list, if failed return and not add to cart
    dishList = readDishList();
    if (dishList == null) {
        alert("Error occured when adding to cart, please refresh the page and try again later.");
        return false;
    }

    // if dish list is fine, read dish name and count from the dishDiv
    let dishName = dishDiv.querySelector('.dish-name')?.textContent;
    let dishCount = dishDiv.querySelector('.dish-count')?.value;

    let dishId = parseInt(getDishFromListName(dishList, dishName)['dish_id']);
    if (dishId == null) {
        return false;
    }
    dishInCart = newcart[dishId];
    if (dishInCart == null) {
        newcart[dishId] = dishCount;
    } else {
        newcart[dishId] = parseInt(dishInCart) + parseInt(dishCount);
    }
    cartSave();
}

function readDishList() {
    let dishListElement = document.querySelector('#dish-all');
    if (!dishListElement) {
        console.log("Dish information missing.")
        return null;
    }
    return JSON.parse(dishListElement.textContent);
}

function getDishFromListName(dishList, dishName) {
    let dishObj = null;
    dishList.forEach(dish => {
        // search for dish id with dishName
        if (dish['dish_name'].valueOf() == dishName) {
            dishObj = dish;
        }
    })
    return dishObj;
}
function getDishFromListId(dishList, dishId) {
    let dishObj = null;
    dishList.forEach(dish => {
        // search for dish id with dishName
        if (dish['dish_id'].valueOf() == dishId) {
            dishObj = dish;
        }
    })
    return dishObj;
}

function cartLoad() {
    newcart = (window.localStorage.getItem('newcart') == null) ?
        {} : JSON.parse(window.localStorage.getItem('newcart'));
}

function cartSave() {
    window.localStorage.setItem('newcart', JSON.stringify(newcart));
}

function cartClear() {
    newcart = {};
    cartSave();
}

function cartSaveFormInput() {
    document.querySelector('#cart-data').value = JSON.stringify(newcart);
}
function cartSubmit() {
    cartSaveFormInput();
    let divForm = document.querySelector('#cart-order-form')
    if (parseInt(divForm.querySelector('#cart-table-number').value)) {
        cartClear();
        divForm.submit();
    } else {
        alert("Please enter your table number.");
    }
}

function cartView() {
    let divCart = document.querySelector('#cart-dishes');
    if (divCart == null) {
        return;
    }
    // Get dish list, if failed return and not add to cart
    dishList = readDishList();
    if (dishList == null) {
        alert("Error occured when loading cart, please refresh the page and try again later.");
        return false;
    }

    // If cart empty, render message to cart
    if (cartIsEmpty()) {
        divEmptyCart = document.createElement('p');
        divEmptyCart.innerHTML = `Your cart is empty. How about adding some <a class="button button-inline" href="/#Featured">Mom's Spaghetti</a>?`
        divCart.appendChild(divEmptyCart)
        return;
    }

    let divDishGrid = document.createElement('div');
    divDishGrid.classList.add('dish-cards-grid');
    for (const [dishId, dishCount] of Object.entries(newcart)) {
        divDishGrid.appendChild(cartCreateCard(dishList, parseInt(dishId), parseInt(dishCount)));
    }

    document.querySelector('#cart-dishes').appendChild(divDishGrid);
    cartSaveFormInput();
}

function cartIsEmpty() {
    return Object.keys(newcart).length === 0;
}

function cartCreateCard(dishList, dishId, dishCount) {
    let dish = getDishFromListId(dishList, dishId);

    let divDishName = document.createElement('div');
    divDishName.classList.add('dish-name', 'font-semibold');
    divDishName.textContent = `${dishCount} x ${dish['dish_name']}`;

    let divDishPrice = document.createElement('div');
    divDishPrice.classList.add('dish-price', 'font-medium');
    divDishPrice.textContent = (dishCount * parseFloat(dish['dish_price'])).toFixed(2);

    let divInfoRow = document.createElement('div');
    divInfoRow.classList.add('dish-info-row');
    divInfoRow.appendChild(divDishName);
    divInfoRow.appendChild(divDishPrice);

    let divInfo = document.createElement('div');
    divInfo.classList.add('dish-info');
    divInfo.appendChild(divInfoRow);


    let buttonCountSub = document.createElement('button');
    buttonCountSub.classList.add('button', 'button-block', 'dish-count-btn', 'dish-count-sub', 'font-medium');


    let inputCount = document.createElement('input');
    inputCount.classList.add('dish-count');
    inputCount.type = "number";
    inputCount.min = "1";
    inputCount.max = "10";
    inputCount.maxlength = "2";
    inputCount.value = dishCount;

    let buttonCountAdd = document.createElement('button');
    buttonCountAdd.classList.add('button', 'button-block', 'dish-count-btn', 'dish-count-add', 'font-medium');

    let divOrderRow = document.createElement('div');
    divOrderRow.classList.add('dish-info-row', 'dish-order');
    divOrderRow.appendChild(buttonCountSub);
    divOrderRow.appendChild(inputCount);
    divOrderRow.appendChild(buttonCountAdd);
    buttonCountSub.addEventListener('click', () => {
        if (inputCount.value > 0) {
            inputCount.value = parseInt(inputCount.value) - 1;
            newcart[dishId] = parseInt(inputCount.value)
        }
    });
    buttonCountAdd.addEventListener('click', () => {
        if (inputCount.value < MAX_ORDER_COUNT) {
            inputCount.value = parseInt(inputCount.value) + 1;
            newcart[dishId] = parseInt(inputCount.value)
        }
    });


    let divDishCard = document.createElement('div');
    divDishCard.classList.add('dish-card', `dish-${dishId}`);
    divDishCard.appendChild(divInfo);
    divDishCard.appendChild(divOrderRow);

    return divDishCard;
}

function cartCardSetButtonCountSub(button, dishId) {

}

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
    const filterToggles = document.querySelector('#allergen-grid').querySelectorAll('input');
    return Array.from(filterToggles)
        .filter(toggle => toggle.checked) // select only checked toggles
        .map(toggle => toggle = toggle.value); // get filter value of checked toggles
}

// Function for filtering menu items with filter checkboxes
function filterMenuCheckbox() {
    filterMenu(filterMenuGetChecked());
}

// Function to show or hide unavailable dishes based on filter toggle state
function showHideUnavailableDishes() {
    const showUnavailable = document.querySelector('#show-unavailable-grid').querySelector('input').checked;
    const unavailableDishCards = document.querySelectorAll('.dish-unavailable');
    unavailableDishCards.forEach(dishCard => {
        dishCard.style.display = showUnavailable ? "grid" : "none";
    })
}

// Function to be called when applying filters from menu
function applyFilters() {
    showHideUnavailableDishes();
    filterMenuCheckbox();
}

// Function to reset all filter toggles and resets menu view
function resetFilters() {
    document.querySelectorAll('.menu-filter-grid').forEach(filterGrid => {
        filterGrid.querySelectorAll('input').forEach(toggle => {
            toggle.checked = false;
        });
    });
    applyFilters();
}

// Checking if enter key is pressed in the search bar to start filtering.
const searchInput = document.querySelector('#Search')
searchInput.addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        e.preventDefault();
        const term = searchInput.value.toLowerCase();
        searchFilter(term);
    }
});

//function for filtering with the search term
function searchFilter(term) {
    const dishCards = document.querySelectorAll('.dish-card');
    dishCards.forEach(dishCard => {
        const dishName = dishCard.querySelector('.dish-name').textContent.toLowerCase();
        if (dishName.includes(searchInput.value.toLowerCase())) {
            dishCard.style.display = 'grid';
        } else {
            dishCard.style.display = 'none';
        }
    })
}

