import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';

class ChatScreen extends StatelessWidget {
  const ChatScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: ListView.builder(
        itemCount: 10,
          itemBuilder: (ctx, index) => Container(
              padding: EdgeInsets.all(8),
              child: Text('This works!'),
          ),
      ),
      floatingActionButton: FloatingActionButton(
        child: Icon(Icons.add),
        onPressed: () {
          FirebaseFirestore.instance
              .collection('chats/V3uNKHWjupM30wEGRLpv/messages')
              .get()
              .then((QuerySnapshot querySnapshot) {
                querySnapshot.docs.forEach((doc) {
                  print(doc["text"]);
                });
              });
              
          /*FirebaseFirestore.instance
              .collection('chats/Q6JTeCrEETEnR8ku8FG8/messages')
              .snapshots()
              .listen((QuerySnapshot querySnapshot) {
            querySnapshot.docs.forEach((doc) {
              print(doc["text"]);
            });
          });*/
        }
      ),
    );
  }
}
