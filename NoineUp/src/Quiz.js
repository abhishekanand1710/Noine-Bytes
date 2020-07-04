import * as React from 'react';
import { Text, View, StyleSheet, Image, TouchableOpacity, ScrollView, WebView } from 'react-native';
import firebase from 'firebase';
export default class Quiz extends React.Component {
  state = { answeredques: {},keys:{},usn:'', started:false,resUrl: null, history:null, ablLevel:0.3, rank:0,quesid:2 , questions:null,curQuesId:null, ques:"", op1:null, op2:null, op3:null, op4:null, currAns:null, selected:null, answerStatus:1};

  static navigationOptions = {
    header: null,
  };


  componentDidMount() {
      answered = []
    firebase.database().ref(`users/${firebase.auth().currentUser.uid}`).on('value',(ques)=>{
        

        firebase.database().ref('quiz/Python').on('value',(question)=>{
            this.setState({flag:true, rank:ques.val().rank, questions:question.val(), ablLevel: ques.val().ablLevel})
        })

        
    })

    
    
  }

  async nextQues()
  {
    var status = true;

    if(this.state.selected == this.state.currAns.toLowerCase())
    {
        status = 1;
    }
    else
        status = 0;

    console.log(status)
    var quesid = this.state.quesid

    
        firebase.database().ref(`users/${firebase.auth().currentUser.uid}`).update({
            ablLevel:this.state.ablLevel 
        },()=>{
    firebase.database().ref(`users/${firebase.auth().currentUser.uid}/quiz/${(99999999999-Math.floor(Date.now() / 1000))}`).set({
        quesid : this.state.quesid,
        status : status,
        abilityLevel : this.state.ablLevel 
    }, ()=>{
        this.setState({answerStatus:status}, ()=>{
            this.conatctApi()
        })
    })

    //await send(this.state.ablLevel, quesid, status, )
    // requestQuestion()
  })
}

  endQuiz()
  {
    this.setState({started:false})
  }

  async conatctApi() {
    console.log("processing")
    try {
        var url = "http://192.168.137.189:5000/flow?ablLevel="+this.state.ablLevel+"&quesid="+this.state.quesid+"&status="+this.state.answerStatus+"&history={1:0,2:1}"
      console.log(url)
        fetch(
        url
        //'http://192.168.1.7:5000/plate?url=https://i.ibb.co/7RLK4PM/test1.jpg'
      ).then(
        res => res.json()
      ).then(
        js =>{
            console.log(js)
        this.setState({ques:js.quesObj.Questions, op1:js.quesObj.Op1,
        op2:js.quesObj.Op2,op3:js.quesObj.Op3,op4:js.quesObj.Op4,
        currAns:js.quesObj.Correct_Answer,ablLevel:js.ablLevel,resUrl:js.resUrl,quesid:js.quesid, started:true})
        }
      
      )
      

    } catch (error) {
      console.error(error);
    }
  }


  async requestQuestion()
  {     // history = []
      //await receieve(ablLevel, quesNo, quesObj, resUrl, HisNo).then(()=>{
      //  firebase.database().ref(`users/${firebase.auth().currentUser.uid}/quiz`).on('value',(ques)=>{
      //  Object.values(ques.val()).map(id => { if(ctr != HisNo) history.push({id : id.quesid, status: id.status}) ctr++ })
      // this.setState({ history:history,  ablLevel : ablLevel, quesid: quesNo}, ()=> {
          // firebase.database().ref().set({ablLevel})
      //})
      //})
    await this.conatctApi()
  }

  renderQues(){
      if(!this.state.started)
      {
          return <View>

                <View style={{heigth:'60%', width:'100%', alignItems:'center', justifyContent:'center', marginTop:50, marginBottom:50}}>
                    <Text style={{fontSize:23, color:'#0a1a29', marginBottom:20}}>Welcome Back!</Text>
                    <Text style={{fontSize:20, color:'#0a1a29', marginBottom:30}}>Your Rank is {this.state.rank}</Text>
                    <View style={{alignItems:'center'}}>
                    <Text style={{fontSize:18, color:'#0a1a29'}}>Rules</Text>
                    <Text style={{fontSize:15, color:'#0a1a29'}}>Correct answer the score is +2</Text>
                    <Text style={{fontSize:15, color:'#0a1a29'}}>Wrong answer the score is -4</Text>
                    <Text style={{fontSize:15, color:'#0a1a29'}}>Unattempted answer the score is 0</Text>
                    </View>
                </View>
                <View style={{alignItems:'center'}}>
              <TouchableOpacity style={{ backgroundColor: '#4CAF50', width:'80%', height:50, justifyContent:'center', borderRadius:20}} onPress={this.requestQuestion.bind(this)}>
          <Text style={{textAlign: 'center',color :'#fff',fontSize: 16, fontStyle:'bold'}}>Start Quiz</Text>
  </TouchableOpacity>
  </View>
              </View>
      }
      else
      {
          
        return <View style={{marginTop:60, alignItems:'center'}}>
        <Text style={{fontSize:23, color:'#0a1a29', marginBottom:35, alignSelf:'center'}}>{this.state.ques}</Text>
        <View style={{width:'80%'}}>
                <View>
                    <TouchableOpacity style={{backgroundColor:(this.state.selected=="op1")?"#4DB6AC":"#448AFF",padding:6, borderRadius:10, marginBottom:7}} onPress={
                        ()=>{
                        this.setState({selected:"op1"})
                        }
                    }>
                    <Text style={{color:'#000',marginBottom:5}}>a) {this.state.op1}</Text> 
                    </TouchableOpacity>
                </View>


                <View>
                    <TouchableOpacity style={{backgroundColor:(this.state.selected=="op2")?"#4DB6AC":"#448AFF",padding:6, borderRadius:10, marginBottom:7}} onPress={
                        ()=>{
                        this.setState({selected:"op2"})
                        }
                    }>
                    <Text style={{color:'#000',marginBottom:5}}>b) {this.state.op2}</Text> 
                    </TouchableOpacity>
                </View>


                <View>
                    <TouchableOpacity style={{backgroundColor:(this.state.selected=="op3")?"#4DB6AC":"#448AFF",padding:6, borderRadius:10, marginBottom:7}} onPress={
                        ()=>{
                        this.setState({selected:"op3"})
                        }
                    }>
                    <Text style={{color:'#000',marginBottom:5}}>c) {this.state.op3}</Text> 
                    </TouchableOpacity>
                </View>

                <View>
                    <TouchableOpacity style={{backgroundColor:(this.state.selected=="op4")?"#4DB6AC":"#448AFF",padding:6, borderRadius:10, marginBottom:7}} onPress={
                        ()=>{
                        this.setState({selected:"op4"})
                        }
                    }>
                    <Text style={{color:'#000',marginBottom:5}}>d) {this.state.op4}</Text> 
                    </TouchableOpacity>
                </View>
        </View>
        <View style={{width:'80%', marginTop:30}}>
        <View>
            <TouchableOpacity style={{ backgroundColor: '#4CAF50', height:50, justifyContent:'center', borderRadius:20, marginBottom:10}} onPress={this.nextQues.bind(this)}>
                <Text style={{textAlign: 'center',color :'#fff',fontSize: 16, fontStyle:'bold'}}>Submit Answer</Text>
            </TouchableOpacity>
        </View>
        <View>
            <TouchableOpacity style={{ backgroundColor: '#4CAF50', height:50, justifyContent:'center', borderRadius:20, marginBottom:10}} onPress={this.nextQues.bind(this)}>
                <Text style={{textAlign: 'center',color :'#fff',fontSize: 16, fontStyle:'bold'}}>Skip Question</Text>
            </TouchableOpacity>
        </View>
        <View>
            <TouchableOpacity style={{ backgroundColor: '#4CAF50', height:50, justifyContent:'center', borderRadius:20}} onPress={this.endQuiz.bind(this)}>
                <Text style={{textAlign: 'center',color :'#fff',fontSize: 16, fontStyle:'bold'}}>Quit Quiz</Text>
            </TouchableOpacity>
        </View>
        </View>
        </View>
      }
  }

  render() {
    console.log(this.state)
    let counter = 0
    return(
      <View style={{ width:'100%', height:'100%'}}>
      <View style={{height:'10%', width:'100%', backgroundColor:'#272727', alignItems:'center',justifyContent:'center',elevation:12, marginBottom:10 }}>
        <Text style={{color:'orange', fontSize:22}}>Noine Quiz</Text>
      </View>
      {this.renderQues()}
    </View>
    );
  }
}