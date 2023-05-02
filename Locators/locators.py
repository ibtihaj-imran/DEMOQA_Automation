from selenium.webdriver.common.by import By


class DataenterLocators:
    Elemnet = "div:nth-child(1) >div >div.card-up"
    WebTables = "div.element-list.collapse.show #item-3"
    Addbutton = "#addNewRecordButton"
    FirstName = "#firstName"
    LastName = "#lastName"
    Email = "#userEmail"
    Age = "#age"
    Salary = "#salary"
    Department = "#department"
    Submit = "#submit"


class EditdataLocators:
    Element = "div:nth-child(1) >div >div.card-up"
    WebTables = "div.element-list.collapse.show #item-3"
    EditButton = "#edit-record-2"
    FirstName = "#firstName"
    LastName = "#lastName"
    Submit = "#submit"


class DraganddropLocators:
    Interactions = "div:nth-child(5) div.card-up"
    Droppable = "div.element-list.collapse.show #item-3"
    MoveButton = "#toolTipButton"
    DragBox = (By.CSS_SELECTOR, "#draggable")
    DropArea =(By.CSS_SELECTOR, "#simpleDropContainer p")


class ImageLocators:
    Element = "div:nth-child(1) >div >div.card-up"
    BrokenLinksImg = "div.element-list.collapse.show #item-6"


class ProgressbarLocators:
    Widget = "div:nth-child(4) div.card-up"
    ProgressBar = 'div.element-list.collapse.show #item-4'
    StartButton = "#startStopButton"


class TooltipLocators:
    Widget = "div:nth-child(4) div.card-up"
    ToolTips = "div.element-list.collapse.show #item-6"
    MoveButton = "#toolTipButton"


class FormLocators:
    Forms = "div:nth-child(2) > div > div.card-up"
    PractiseForm = "div.element-list.collapse.show"
    FirstName = "#firstName"
    LastName = "#lastName"
    Email = "#userEmail"
    Gender = "label[for='gender-radio-1']"
    Mobile = "#userNumber"
    DateofBirth = "#dateOfBirthInput"
    YearSelect = (By.CSS_SELECTOR, ".react-datepicker__year-select")
    MonthSelect = (By.CSS_SELECTOR, ".react-datepicker__month-select")
    DateSelect = "div[aria-label='Choose Monday, January 15th, 1990']"
    Subjects = "#subjectsInput"
    Hobbies = "label[for='hobbies-checkbox-2']"
    SelectImage = "#uploadPicture"
    CurrentAddress = "#currentAddress"
    State = "#state div.css-1wa3eu0-placeholder"
    Selectstate = "#react-select-3-input"
    City = "#stateCity-wrapper > div:nth-child(3)"
    SelectCity = "#react-select-4-input"
    Interactions = "div.left-pannel div:nth-child(5)"
    Submit = "#submit"
