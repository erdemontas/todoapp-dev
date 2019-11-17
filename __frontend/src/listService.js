import axios from 'axios';
const API_URL = 'http://localhost:8000';

export default class listService{

    constructor(){}


    getCustomers() {
        const url = `${API_URL}/api/todoitems/`;
        return axios.get(url).then(response => response.data);
    }  
    getCustomer(pk) {
        const url = `${API_URL}/api/todoitems/${pk}`;
        return axios.get(url).then(response => response.data);
    }
    deleteCustomer(customer){
        const url = `${API_URL}/api/todoitems/${customer.pk}`;
        return axios.delete(url);
    }
    createCustomer(customer){
        const url = `${API_URL}/api/todoitems/`;
        return axios.post(url,todoitem);
    }
    updateCustomer(customer){
        const url = `${API_URL}/api/todoitems/${customer.pk}`;
        return axios.put(url,customer);
    }
}