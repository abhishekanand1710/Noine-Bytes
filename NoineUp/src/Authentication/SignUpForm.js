import React, { Component } from 'react';
import { Text, View, Image,
    TouchableWithoutFeedback,
    TextInput, Keyboard, TouchableOpacity, ToastAndroid, ActivityIndicator,
    Picker
     } from 'react-native';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view';
import firebase from 'firebase';

export default class SignUp extends Component {
    static navigationOptions = {
        headerMode: 'none'
      }

      state={email:'', password:'', username:'',  category:'',signUpstatus:false, phone:''}

      firebaseSignUp() {
        const email = this.state.email
        const password = this.state.password
        const { navigate } = this.props.navigation;

        if(this.state.email==''&&this.state.password==''&&this.state.category==''&&this.state.username==''&&this.state.phone=='')
        {
            ToastAndroid.show('Please fill all the fields', ToastAndroid.SHORT);
        }
        else{
            var cat = "user";
            if(this.state.category == "2")
                cat = "User";
            else
                cat = "Admin"
        firebase.auth().createUserWithEmailAndPassword(email,password).then(
            ()=>{



                firebase.database().ref().child('users').child(firebase.auth().currentUser.uid).set({
                    email: this.state.email,
                    username: this.state.username,
                    phone:this.state.phone,
                    category: cat,
                    score: 0
                   },()=>{
                    this.props.navigation.navigate('HomeNavi', {screen:'quiz'})
                   })
            }
        )
        .catch(() => {
            ToastAndroid.show('Invalid Credentials', ToastAndroid.SHORT);
          })
        
        }
    }

    

        renderSpinnerButton(){
            if(!this.state.signUpstatus)
            {
                return (<TouchableOpacity style={{backgroundColor:'#4CAF50',height:50, justifyContent:'center', borderRadius:20, width:'60%'}} onPress={()=>{
                    this.setState({signUpstatus:true},
                        this.firebaseSignUp.bind(this)
                    )
                }}>
                    <Text style={{textAlign: 'center',color :'#fff',fontSize: 16, fontStyle:'bold'}}>SIGN UP</Text>
                </TouchableOpacity>);
            }
            else
            {
                return <ActivityIndicator size={'large'} color="#4CAF50"/>
            }
        }

    render() {
        return (
            <KeyboardAwareScrollView style={{flex:1,backgroundColor: '#0a1a29',flexDirection: 'column'}}>
            <View style={{flex:1, alignItems:'center'}}>
                        <Image style={{width:100 , height:100, alignSelf:'center', marginTop:50, marginBottom:50, tintColor:'#fff'}}
                            source={require('../Resources/Images/logo.png')}>
                        </Image>
                        <TextInput style={{ width:'80%',
                                            height: 40,
                                        color: '#fff',
                                        marginBottom: 20,
                                        borderWidth:2,
                                        borderColor:'#4CAF50',
                                        paddingHorizontal: 10}}
                            placeholder="Enter username"
                            autoCorrect={false}
                            placeholderTextColor='#fff'
                            onChangeText={username=>{this.setState({username:username})}}
                            value={this.state.username}
                        />
                        <TextInput style={{ width:'80%',
                                            height: 40,
                                        color: '#fff',
                                        borderWidth:2,
                                        borderColor:'#4CAF50',
                                        marginBottom: 20,
                                        paddingHorizontal: 10}}
                            placeholder="Enter email"
                            autoCorrect={false}
                            placeholderTextColor='#fff'
                            onChangeText={email=>{this.setState({email:email})}}
                            value={this.state.email}
                        />
                        <TextInput style={{width:'80%',
                                            height: 40,
                                        color: '#fff',
                                        borderWidth:2,
                                        borderColor:'#4CAF50',
                                        marginBottom: 20,
                                        paddingHorizontal: 10}}
                            placeholder="Enter Password"
                            secureTextEntry
                            placeholderTextColor='#fff'
                            onChangeText={password=>{this.setState({password:password})}}
                            value={this.state.password}
                            autoCorrect={false}
                        />
                        <TextInput style={{width:'80%',
                                            height: 40,
                                        color: '#fff',
                                        borderWidth:2,
                                        borderColor:'#4CAF50',
                                        marginBottom: 20,
                                        paddingHorizontal: 10}}
                            placeholder="Enter Phone Number"
                            onChangeText={phone=>{this.setState({phone:phone})}}
                            value={this.state.phone}
                            placeholderTextColor='#fff'
                            autoCorrect={false}
                        />


                        <View style={{height:43, width:'80%',
                                marginBottom:10,
                                borderWidth:2,
                                borderColor:'#4CAF50',}}>
                        <Picker
                            style={{width: '100%',
                                height: 38,
                                color:'#fff',
                                paddingRight: 5,
                                paddingLeft: 5,
                                borderRadius:20,
                                marginBottom: 20}}
                            mode="dropdown"
                            selectedValue = {this.state.category}
                            onValueChange= {(itemValue, itemIndex) => this.setState({ category: itemValue })}
                            >
                            <Picker.Item label="Choose Category" value="0" />
                            <Picker.Item label="Admin" value="1" />
                            <Picker.Item label="User" value="2" />
                      </Picker>
                      </View>

                        <View style={{width:'80%', height:50, justifyContent:'center',alignItems:'center'}}>
                            {this.renderSpinnerButton()}
                        </View>

                        </View>
                        </KeyboardAwareScrollView>
        );
    }
}
