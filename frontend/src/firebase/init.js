// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getFirestore } from 'firebase/firestore/lite';
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDbf7CxNP4Ce26wNilKl53ESlOZOgh-VXI",
  authDomain: "mms-project-65106.firebaseapp.com",
  projectId: "mms-project-65106",
  storageBucket: "mms-project-65106.appspot.com",
  messagingSenderId: "1034646575037",
  appId: "1:1034646575037:web:0750b961356ec5a3d164d4",
  measurementId: "G-KH24W3Y2R2"
};

// Initialize Firebase
initializeApp(firebaseConfig)
const db = getFirestore();
export default db;

