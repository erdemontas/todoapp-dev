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

