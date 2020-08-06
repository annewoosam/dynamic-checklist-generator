
// Create needed constants - form field names plus Input

//Creator constants
const list = document.querySelector('ul');
const titleInput = document.querySelector('#title');
const bodyInput = document.querySelector('#body');
const checklistNameInput = document.querySelector('#checklistName');
const questionPromptInput = document.querySelector('#questionPrompt');
const answerYesInput = document.querySelector('#answerYes');
const answerNoInput = document.querySelector('#answerNo');
const answerNAInput = document.querySelector('#answerNA');
const helpTextInput = document.querySelector('#helpText');
const videoURLInput = document.querySelector('#videoURL');
const categoryInput = document.querySelector('#category');
const driverInput = document.querySelector('#driver');

// Preparer chooses checklist then populates following items
const preparerNameInput = document.querySelector('#preparerName');
const preparerEmailInput = document.querySelector('#preparerEmail');
const preparationStartDateInput = document.querySelector('#preparationStartDate');
const preparationWhoForInput = document.querySelector('#preparationWhoFor');
const reviewerNameInput = document.querySelector('#reviewerName');
const reviewerEmailInput = document.querySelector('#reviewerEmail');
const preparerMinutesInput = document.querySelector('#preparerMinutes');
//Reviewer notified to review then populates the following items
const reviewStartDateInput = document.querySelector('#reviewStartDate');
const recipientNameInput = document.querySelector('#recipientName');
const recipientEmailInput = document.querySelector('#recipientEmail');
const reviewerMinutesInput = document.querySelector('#reviewerMinutes');

//Form & Buttons

//Creator  - later will split out for Preparer & Reviewer
const form = document.querySelector('form');
const submitBtn = document.querySelector('form button');


// Create an instance of a db object for us to store the open database in
let db;
window.onload = function() {

};
// Open our database; it is created if it doesn't already exist
// (see onupgradeneeded below)
let request = window.indexedDB.open('notes_db', 1);
// onerror handler signifies that the database didn't open successfully
request.onerror = function() {
  console.log('Database failed to open');
};

// onsuccess handler signifies that the database opened successfully
request.onsuccess = function() {
  console.log('Database opened successfully');

  // Store the opened database object in the db variable. This is used a lot below
  db = request.result;

  // Run the displayData() function to display the notes already in the IDB
  displayData();
};
// Setup the database tables if this has not already been done
request.onupgradeneeded = function(e) {
  // Grab a reference to the opened database
  let db = e.target.result;

  // Create an objectStore to store our notes in (basically like a single table)
  // including a auto-incrementing key
  let objectStore = db.createObjectStore('notes_os', { keyPath: 'id', autoIncrement:true });

  // Define what data items the objectStore will contain - basically field name repeated twice
  
  //Creator objectstores
  objectStore.createIndex('title', 'title', { unique: false });
  objectStore.createIndex('body', 'body', { unique: false });
  objectStore.createIndex('checklistName', 'checklistName', { unique: false });
  objectStore.createIndex('questionPrompt', 'questionPrompt', { unique: false });
  objectStore.createIndex('answerYes', 'answerYes', { unique: false });
  objectStore.createIndex('answerNo', 'answerNo', { unique: false });
  objectStore.createIndex('answerNA', 'answerNA', { unique: false });
  objectStore.createIndex('helpTest', 'helpTest', { unique: false });
  objectStore.createIndex('videoURL', 'videoURL', { unique: false });
  objectStore.createIndex('category', 'category', { unique: false });
  objectStore.createIndex('driver', 'driver', { unique: false });
  
  //Preparer objectstores

  objectStore.createIndex('preparerName', 'preparerName', { unique: false });
  objectStore.createIndex('preparerEmail', 'preparerEmail', { unique: false });
  objectStore.createIndex('preparationStartDate', 'preparationStartDate', { unique: false });
  objectStore.createIndex('preparationWhoFor', 'preparationWhoFor', { unique: false });
  objectStore.createIndex('reviewerName', 'reviewerName', { unique: false });
  objectStore.createIndex('reviewerEmail', 'reviewerEmail', { unique: false });
    objectStore.createIndex('preparerMinutes', 'preparerminutes', { unique: false });
  //Review ObjectStores
  
  objectStore.createIndex('reviewStartDate', 'reviewStartDate', { unique: false });
  objectStore.createIndex('recipientName', 'recipientName', { unique: false });
  objectStore.createIndex('recipientEmail', 'recipientEmail', { unique: false });
       objectStore.createIndex('reviewerMinutes', 'reviewerMinutes', { unique: false });              
  console.log('Database setup complete');
};
// Create an onsubmit handler so that when the form is submitted the addData() function is run
form.onsubmit = addData;
// Define the addData() function
function addData(e) {
  // prevent default - we don't want the form to submit in the conventional way
  e.preventDefault();

  // grab the values entered into the form fields and store them in an object ready for being inserted into the DB
  // placed one per line so can maintain more easily
  
  let newItem = {
  title: titleInput.value,
  body: bodyInput.value,
  checklistName: checklistNameInput.value,
  questionPrompt: questionPromptInput.value,
  answerYes: answerYesInput.value,
  answerNo: answerNoInput.value,
  answerNA: answerNAInput.value,
  helpText: helpTextInput.value,
  videoURL: videoURLInput.value,
  category: categoryInput.value,
  driver: driverInput.value,
  // Preparer newItems
  preparerName: preparerNameInput.value,
  preparerEmail: preparerEmailInput.value,
  preparationStartDate: preparationStartDateInput.value,
  preparationWhoFor: preparationWhoForInput.value,
  reviewerName: reviewerNameInput.value,
  reviewerEmail: reviewerEmailInput.value,
  preparerMinutes: preparerMinutesInput.value,
  // Reviewer newItems
  reviewStartDate: reviewStartDateInput.value,
  recipientName: recipientNameInput.value,
  recipientEmail: recipientEmailInput.value,
  reviewerMinutes: reviewerMinutesInput.value
  };

  // open a read/write db transaction, ready for adding the data
  let transaction = db.transaction(['notes_os'], 'readwrite');

  // call an object store that's already been added to the database
  let objectStore = transaction.objectStore('notes_os');

  // Make a request to add our newItem object to the object store
  let request = objectStore.add(newItem);
  request.onsuccess = function() {
    // Clear the form, ready for adding the next entry
    //Creator Values
    titleInput.value = '';
    bodyInput.value = '';
    checklistNameInput.value = '';
    questionPromptInput.value = '';
    answerYesInput.value = '';
    answerNoInput.value = '';
    answerNAInput.value = '';
    helpTextInput.value = '';
    videoURLInput.value = '';
    driverInput.value = '';
    categoryInput.value = '';
    //Preparer Values
    preparerNameInput.value = '';
    preparerEmailInput.value = '';
    preparationStartDateInput.value = '';
    preparationWhoForInput.value = '';
    reviewerNameInput.value = '';
    reviewerEmailInput.value = ''
    preparerMinutesInput.value = ''
    //Reviewer values
    reviewStartDateInput.value = '';
    recipientNameInput.value = '';
    recipientEmailInput.value = '';
    reviewerMinutesInput.value = ''
  };

  // Report on the success of the transaction completing, when everything is done
  transaction.oncomplete = function() {
    console.log('Transaction completed: database modification finished.');

    // update the display of data to show the newly added item, by running displayData() again.
    displayData();
  };

  transaction.onerror = function() {
    console.log('Transaction not opened due to error');
  };
}
// Define the displayData() function
function displayData() {
  // Here we empty the contents of the list element each time the display is updated
  // If you didn't do this, you'd get duplicates listed each time a new note is added
  while (list.firstChild) {
    list.removeChild(list.firstChild);
  }

  // Open our object store and then get a cursor - which iterates through all the
  // different data items in the store
  let objectStore = db.transaction('notes_os').objectStore('notes_os');
  objectStore.openCursor().onsuccess = function(e) {
    // Get a reference to the cursor
    let cursor = e.target.result;

    // If there is still another data item to iterate through, keep running this code
    if(cursor) {
      // Create a list item, h3, and p... to put each data item inside when displaying it
      // structure the HTML fragment, and append it inside the list
      //For Creator
      const listItem = document.createElement('li');
      const par = document.createElement('li');
      const para = document.createElement('li');
      const para2 = document.createElement('li');
      const para3 = document.createElement('li');
      const para4 = document.createElement('li');
      const para5 = document.createElement('li');
      const para6 = document.createElement('li');
      const para7 = document.createElement('li');
      const para8 = document.createElement('li'); 
      const para9 = document.createElement('li');
      const para10 = document.createElement('li');
      //For Preparer
      const para11 = document.createElement('li');
      const para12 = document.createElement('li');
      const para13 = document.createElement('li');
      const para14 = document.createElement('li');
      const para15 = document.createElement('li');
      const para16 = document.createElement('li');
      //For Reviewer
      const para17 = document.createElement('li');
      const para18 = document.createElement('li');
      const para19 = document.createElement('li');
      //New for Preparer & Reviewer minutes
      const para20 = document.createElement('li');
      const para21 = document.createElement('li');
      //For Creator
      listItem.appendChild(par);
      listItem.appendChild(para);
      listItem.appendChild(para2);
      listItem.appendChild(para3);
      listItem.appendChild(para4);
      listItem.appendChild(para5);
      listItem.appendChild(para6);
      listItem.appendChild(para7);
      listItem.appendChild(para8);
      listItem.appendChild(para9);
      listItem.appendChild(para10);
      //For Preparer
      listItem.appendChild(para11);
      listItem.appendChild(para12);
      listItem.appendChild(para13);
      listItem.appendChild(para14);
      listItem.appendChild(para15);
      listItem.appendChild(para16);
      //For Reviewer
      listItem.appendChild(para17);
      listItem.appendChild(para18);
      listItem.appendChild(para19);
      //New for Preparer & Reviewer minutes
      listItem.appendChild(para20);
      listItem.appendChild(para21);
            
      list.appendChild(listItem);

      // Put the data from the cursor inside the para.
      
      //Creator data
      par.textContent = cursor.value.title;
      para.textContent = cursor.value.body;
      para2.textContent = cursor.value.checklistName;
      para3.textContent = cursor.value.questionPrompt;
      para4.textContent = cursor.value.answerYes;
      para5.textContent = cursor.value.answerNo;
      para6.textContent = cursor.value.answerNA;
      para7.textContent = cursor.value.helpText;
      para8.textContent = cursor.value.videoURL;
      para9.textContent = cursor.value.category;
      para10.textContent = cursor.value.driver;
      //Preparer data
      para11.textContent = cursor.value.preparerName;
      para12.textContent = cursor.value.preparerEmail;
      para13.textContent = cursor.value.preparationStartDate;
      para14.textContent = cursor.value.preparationWhoFor;
      para15.textContent = cursor.value.reviewerName;
      para16.textContent = cursor.value.reviewerEmail;
      //Reviewer data
      para17.textContent = cursor.value.reviewStartDate;
      para18.textContent = cursor.value.recipientName;
      para19.textContent = cursor.value.recipientEmail;
      //New for Preparer & Reviewer minutes
      para20.textContent = cursor.value.preparerMinutes;
      para21.textContent = cursor.value.reviewerMinutes;
      
      // Store the ID of the data item inside an attribute on the listItem, so we know
      // which item it corresponds to. This will be useful later when we want to delete items
      listItem.setAttribute('data-note-id', cursor.value.id);

      // Create a button and place it inside each listItem
      const deleteBtn = document.createElement('button');
      listItem.appendChild(deleteBtn);
      deleteBtn.textContent = 'Delete Question';

      // Set an event handler so that when the button is clicked, the deleteItem()
      // function is run
      deleteBtn.onclick = deleteItem;

      // Iterate to the next item in the cursor
      cursor.continue();
    } else {
      // Again, if list item is empty, display a 'No notes stored' message
      if(!list.firstChild) {
        const listItem = document.createElement('li');
        listItem.textContent = 'No questions stored.';
        list.appendChild(listItem);
      }
      // if there are no more cursor items to iterate through, say so
      console.log('Notes all displayed');
    }
  };
}
// Define the deleteItem() function
function deleteItem(e) {
  // retrieve the name of the task we want to delete. We need
  // to convert it to a number before trying it use it with IDB; IDB key
  // values are type-sensitive.
  let noteId = Number(e.target.parentNode.getAttribute('data-note-id'));

  // open a database transaction and delete the task, finding it using the id we retrieved above
  let transaction = db.transaction(['notes_os'], 'readwrite');
  let objectStore = transaction.objectStore('notes_os');
  let request = objectStore.delete(noteId);

  // report that the data item has been deleted
  transaction.oncomplete = function() {
    // delete the parent of the button
    // which is the list item, so it is no longer displayed
    e.target.parentNode.parentNode.removeChild(e.target.parentNode);
    console.log('Question ' + noteId + ' deleted.');

    // Again, if list item is empty, display a 'No notes stored' message
    if(!list.firstChild) {
      let listItem = document.createElement('li');
      listItem.textContent = 'No questions stored.';
      list.appendChild(listItem);
    }
  };
}