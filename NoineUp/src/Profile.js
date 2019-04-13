import React, { Component } from 'react';
import { View, Text, TouchableOpacity, Image, ToastAndroid, } from 'react-native';
import firebase from 'firebase';

export default class Profile extends Component {
    static navigationOptions = {
        headerMode: 'none'
      }

    state={email:'', username:'', category:'', changePasswordMail:'',phone:'',
}

    componentDidMount()
    {   
        
        firebase.database().ref(`users/${firebase.auth().currentUser.uid}/`).on('value',(user)=>{
            console.log(user.val())
            this.setState({email: user.val().email, username: user.val().username, category: user.val().category, phone:user.val().phone });
        }) 
    }

    firebaseSignOut() {
        firebase.auth().signOut();
    }
    forgotPassword(){
        firebase.auth()
        .sendPasswordResetEmail(this.state.email)
        .then(()=>{
          ToastAndroid.show("Password Reset Link is sent your mail", ToastAndroid.LONG)
        })
        .catch(() => {
          //Function Binding is very necessary in JS as onLoginFail is not bound to the class
          ToastAndroid.show('Please Enter your Email', ToastAndroid.SHORT);
        });
      }

    render() {
        return (
            <View style={{flex:1, backgroundColor:"#0a1a29"}}>
                <View style={{top:0,left:0,right:0, height:50, backgroundColor:'#4CAF50', alignItems:'center', justifyContent:'center'}}>
                    <Text style={{color:'#fff', fontSize:18}}>Profile</Text>
                </View>
        
                <View>
                    <View style={{justifyContent:'center',backgroundColor:'#E0E0E0', height:40}}>
                        <Text style={{marginLeft:14,color:'#000', fontSize:18}}>Account Information</Text>
                    </View>

                    <View style={{ height:40, flexDirection:'row', marginTop:9, borderBottomColor:'#dedede', borderBottomWidth:1}}>
                        <Text style={{width:100, marginLeft:14, fontSize:16, color:'#fff'}}>Name</Text>
                        <Text style={{marginLeft:20, fontSize:16, color:'#fff'}}>{this.state.username}</Text>
                    </View>
                    <View style={{ height:40, flexDirection:'row', borderBottomColor:'#dedede', borderBottomWidth:1, alignItems:'center'}}>
                        <Text style={{width:100, marginLeft:14, fontSize:16, color:'#fff'}}>Email</Text>
                        <Text style={{marginLeft:20, fontSize:16, color:'#fff'}}>{this.state.email}</Text>
                    </View>
                    <View style={{height:40,marginBottom:5, flexDirection:'row', borderBottomColor:'#fff', borderBottomColor:'#dedede', borderBottomWidth:1, alignItems:'center'}}>
                        <Text style={{width:100, marginLeft:14, fontSize:16, color:'#fff'}}>Phone No</Text>
                        <Text style={{marginLeft:20, fontSize:16, color:'#fff'}}>{this.state.phone}</Text>
                    </View>
                    <View style={{height:40,marginBottom:5, flexDirection:'row', borderBottomColor:'#fff', borderBottomWidth:1, alignItems:'center'}}>
                        <Text style={{width:100, marginLeft:14, fontSize:16, color:'#fff'}}>Category</Text>
                        <Text style={{marginLeft:20, fontSize:16, color:'#fff'}}>{this.state.category}</Text>
                    </View>

                    <View style={{justifyContent:'center',backgroundColor:'#E0E0E0', height:40}}>
                        <Text style={{marginLeft:14,color:'#000', fontSize:18}}>Settings</Text>
                    </View>
                    <TouchableOpacity onPress={this.forgotPassword.bind(this)} style={{height:40, flexDirection:'row', marginTop:5,alignItems:'center'}}>
                        <Image style={{width:35, height:35, marginLeft:14, tintColor:'#fff'}} source={require('./Resources/Images/passoword.png')} />
                        <Text style={{marginLeft:12,textAlign:'center', fontSize:16, color:'#000', color:'#fff'}}>Change Password</Text>
                    </TouchableOpacity>

                    <TouchableOpacity onPress={this.firebaseSignOut.bind(this)} style={{marginTop:9,width:'80%', height:60, backgroundColor:'#B71C1C', alignSelf:'center', justifyContent:'center', }}>
                        <Text style={{textAlign:'center', fontSize:18, color:'#fff'}}>SignOut</Text>
                    </TouchableOpacity>
                    
                    </View>
            </View>
        );
    }
}