import  React, { Component } from  'react';
import  TodoListService  from  './TodoListService';

const  todolistService  =  new  TodoListService();

class  TodoList  extends  Component {

constructor(props) {
    super(props);
    this.state  = {
        todolists: []
    };
}

componentDidMount() {
    var  self  =  this;
    todolistService.getTodoLists().then(function (result) {
        console.log(result);
        self.setState({ todolists:  result.data, nextPageURL:  result.nextlink})
    });
}

render() {

    return (
        <div  className="todo--list">
            <table  className="table">
            <thead  key="thead">
            <tr>
                <th>#</th>
                <th>Name</th>
                <th>Description</th>
                <th>Actions</th>
            </tr>
            </thead>
            <tbody>
            {this.state.todolists.map( c  =>
                <tr  key={c.pk}>
                <td>{c.pk}  </td>
                <td>{c.name}</td>
                <td>{c.description}</td>
                <td>
               
                
                </td>
            </tr>)}
            </tbody>
            </table>
           
        </div>
        );
  }
}
export  default  TodoList;