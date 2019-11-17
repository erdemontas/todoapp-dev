import axios from 'axios';

const API_URL = 'http://localhost:8000';

export default class TodoListService{

    constructor(){}


    getTodoLists() {
        const url = `${API_URL}/api/todolists/`;
        console.log(axios.get(url))
        return axios.get(url).then(response => response.data);
    }  
    getTodoList(pk) {
        const url = `${API_URL}/api/todolists/${pk}`;
        return axios.get(url).then(response => response.data);
    }
    deleteTodoList(customer){
        const url = `${API_URL}/api/todolists/${customer.pk}`;
        return axios.delete(url);
    }
    createTodoList(customer){
        const url = `${API_URL}/api/todolists/`;
        return axios.post(url,customer);
    }
    updateTodoList(customer){
        const url = `${API_URL}/api/todolists/${customer.pk}`;
        return axios.put(url,customer);
    }
}

export default class TodoItemService{

    constructor(){}


    getTodoItems() {
        const url = `${API_URL}/api/todoitems/`;
        console.log(axios.get(url))
        return axios.get(url).then(response => response.data);
    }  
    getTodoItem(pk) {
        const url = `${API_URL}/api/todoitems/${pk}`;
        return axios.get(url).then(response => response.data);
    }
    deleteTodoItem(customer){
        const url = `${API_URL}/api/todoitems/${customer.pk}`;
        return axios.delete(url);
    }
    createTodoItem(customer){
        const url = `${API_URL}/api/todoitems/`;
        return axios.post(url,customer);
    }
    updateTodoItem(customer){
        const url = `${API_URL}/api/todoitems/${customer.pk}`;
        return axios.put(url,customer);
    }
}