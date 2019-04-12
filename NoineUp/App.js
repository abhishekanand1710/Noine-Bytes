
import React, {Component} from 'react';
import {View, Alert, NetInfo, ToastAndroid } from 'react-native';
import firebase from 'firebase';
import TabNavi from './src/TabNavi';
import StackNavi from './src/StackNavi';

import Login from './src/Authentication/LoginForm';

export default class App extends Component {

  

  state={loggedIn:false , allow: false, connectionInfo:'' }
  
  componentWillMount(){
    // Initialize Firebase
    if (!firebase.apps.length) {
      const config = {
        apiKey: "AIzaSyC36YXzKZVjc-fjmIEYpWsKQu1FGiQZYik",
        authDomain: "noineup.firebaseapp.com",
        databaseURL: "https://noineup.firebaseio.com",
        projectId: "noineup",
        storageBucket: "noineup.appspot.com",
        messagingSenderId: "292492625676"
      };
      firebase.initializeApp(config);

      firebase.auth().onAuthStateChanged(user => {
        if (user) {
            this.setState({ loggedIn: true });
        } else {
          this.setState({ loggedIn: false });
        }
      });
    }

  }

  renderScreens(){
    switch(this.state.loggedIn)
    {
      case true:
        return <TabNavi />;
      case false:
        return <StackNavi />;
    }
  }
  

  render() {
    return (
      <View style={{flex:1}}>
        {this.renderScreens()}
      </View>
    );
  }
}


