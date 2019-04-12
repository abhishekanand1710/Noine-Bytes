import React, {Component} from 'react';
import {StyleSheet, Text, View, Image,
    TouchableWithoutFeedback, StatusBar,
    TextInput, SafeAreaView, Keyboard, TouchableOpacity,
     Dimensions, ToastAndroid, ActivityIndicator} from 'react-native';
import firebase from 'firebase';

import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view';

export default class Login extends Component{
    state={email:'', password:'', spinnerState:false}

    static navigationOptions = {
        header: null
    }

    firebaseSignIn() {
        const email = this.state.email
        const password = this.state.password

        firebase.auth().signInWithEmailAndPassword(email,password).then(
            ()=>{
                this.props.navigation.navigate('HomeNavi', {screen:'quiz'})
            }
        )
        .catch(() => {
            ToastAndroid.show('Invalid Credentials', ToastAndroid.SHORT);
            this.setState({spinnerState:false})
          });
    }

    signIn(){
        this.setState({spinnerState:true},()=>{
            this.firebaseSignIn()
        })
    }

    signUp() { 
            this.props.navigation.navigate('SignUp', {screen:'SignUp'})
    }

    loadSpinnerButton(){

        if(this.state.spinnerState)
        {
            return <View style={{marginTop:10}}><ActivityIndicator size="large" color="#4CAF50"/></View>
        }
        else{
            return <View style={{width:'80%', height:50, justifyContent:'space-between', flexDirection:'row', marginTop:10}}>
            <TouchableOpacity style={{ backgroundColor: '#4CAF50', width:'100%', height:50, justifyContent:'center', borderRadius:20}} onPress={this.signIn.bind(this)}>
                    <Text style={{textAlign: 'center',color :'#fff',fontSize: 16, fontStyle:'bold'}}>SIGN IN</Text>
            </TouchableOpacity>
        </View>
        }                
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
            <KeyboardAwareScrollView style={{width:'100%',height:'100%',backgroundColor: '#0a1a29',flexDirection: 'column'}} >
                <TouchableWithoutFeedback style={{width:'100%',height:'100%',backgroundColor: '#4857cb',flexDirection: 'column'}} 
                                                  onPress={Keyboard.dismiss}>
                <View style={{justifyContent: 'center',width:'100%',height:'100%', alignItems:'center'}}>
                <View style={{top:0,left:0,right:0, height:60, backgroundColor:'#4CAF50', alignItems:'center', justifyContent:'center', width:'100%', borderBottomRightRadius:30, borderBottomLeftRadius:30}}>
                    <Text style={{color:'#fff', fontSize:18}}>Noine Up</Text>
                </View>
                        <Image style={{width:100, height:100,marginTop:70,marginBottom:100, alignSelf:'center', tintColor:'#fff' }}
                            source={ require('../Resources/Images/logo.png')}>
                        </Image>

                        <View style={{alignItems:'center'}}>
                            <View style={{flexDirection:'row', width:'80%',borderWidth:2, borderColor:'#4CAF50', borderRadius:20, height:43}}>
                                <View style={{width:'20%', height:40, alignItems:'center', justifyContent:'center', borderTopLeftRadius:20, borderBottomLeftRadius:20}}>
                                <Image source={require('../Resources/Images/email.png')} style={{width:33, height:33, tintColor:'#fff'}} />
                                </View>
                                <TextInput style={{ width:'80%',
                                                    height: 40,
                                                color: '#fff',
                                                borderTopRightRadius:20,
                                                borderBottomRightRadius:20}}
                                    placeholder="Enter username/email"
                                    keyboardType='email-address'
                                    returnKeyType='next'
                                    placeholderTextColor='#fff'
                                    autoCorrect={false}
                                    onChangeText={email=>{this.setState({email:email})}}
                                    value={this.state.email}
                                    onSubmitEditing={()=> this.refs.txtPassword.focus()}
                                />
                            </View>
                            <View style={{flexDirection:'row', width:'80%', marginTop:10, borderColor:'#4CAF50', borderWidth:2, borderRadius:20, height:43}}>
                                <View style={{width:'20%',  height:40, alignItems:'center', justifyContent:'center', borderTopLeftRadius:20, borderBottomLeftRadius:20}}>
                                <Image source={require('../Resources/Images/passoword.png')} style={{width:33, height:33, tintColor:'#fff'}} />
                                </View>
                                <TextInput style={{width:'80%',
                                            height: 40,
                                    color: '#fff',
                                    marginBottom: 15,
                                    borderTopRightRadius:20,
                                    borderBottomRightRadius:20}}
                                    placeholder="Enter password"
                                    returnKeyType='go'
                                    secureTextEntry
                                    placeholderTextColor='#fff'
                                    onChangeText={password=>{this.setState({password:password})}}
                                    value={this.state.password}
                                    autoCorrect={false}
                                    ref={"txtPassword"}
                                />
                            </View>

                        
                        </View>
                        {
                            this.loadSpinnerButton()
                        }
                        
                        <View style={{width:'80%', height:50, justifyContent:'space-between', flexDirection:'row'}}>
                            <TouchableOpacity style={{ width:'45%', height:50, justifyContent:'center', borderRadius:20}} onPress={this.forgotPassword.bind(this)}>
                                    <Text style={{textAlign: 'center',color :'#4CAF50',fontSize: 16, fontStyle:'bold'}}>Forgot Password?</Text>
                            </TouchableOpacity>

                            <TouchableOpacity style={{ width:'45%', height:50, justifyContent:'center', borderRadius:20}} onPress={this.signUp.bind(this)}>
                                    <Text style={{textAlign: 'center',color :'#4CAF50',fontSize: 16, fontStyle:'bold'}}>Create Account</Text>
                            </TouchableOpacity>
                        </View>

                        {/*
                        <Text style={{fontSize:16, color:'#4CAF50', marginTop:25}}>OR SIGN IN USING</Text>

                        <View style={{alignItems:'center'}}>
                        <View style={{width:'80%', height:50, marginTop:15 , alignItems:'center', flexDirection:'row'}}>
                            <TouchableOpacity style={{justifyContent:'center',paddingRight:20}} onPress={()=>{}}>
                                    <Image source={require('../../Resources/Images/google.png')} style={{width:40, height:40}} />
                            </TouchableOpacity>

                            <TouchableOpacity style={{justifyContent:'center',paddingLeft:20}} onPress={()=>{}}>
                            <Image source={require('../../Resources/Images/facebook.png')} style={{width:50, height:50}} />
                            </TouchableOpacity>
                        </View>
                        </View>
                        */}
                </View>
            </TouchableWithoutFeedback>
        </KeyboardAwareScrollView>
        );
    }
}
