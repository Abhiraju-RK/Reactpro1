import { userState } from 'react';
import AddStudent from './components/AddStudent';
import StudentList from './components/StudentList';

function App(){
  const [students,setstudents]=userState([]);
  const addstudent=(student)=>{
    setstudents([...students,student])

  };
  return(
    <div>
      
    </div>
  )
}
