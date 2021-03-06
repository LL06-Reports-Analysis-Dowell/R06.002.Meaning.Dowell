#the following is the R code for determining the word's type and then posting the question.

install.packages("udpipe") # This is the package required for determinig whether the word is a noun or not

library(udpipe) # loading the package
model<-udpipe_download_model(language = "english") # downloading the language for determing the POS of the word
model<-udpipe_load_model(model$file_model)#loading the model in the variable 'model'
# now we will create a function which will first determine the part of speech, if the word is noun it will ask the queston
noun<-function(verb,word){ #we will take two inputs from te user, one is the auxillary verb and the other is the word itself
  x<-udpipe_annotate(model,x=word)
  x<-as.data.frame(x)
  x$upos #this stores the parts of speech of the word
  if(x$upos=="NOUN"){ #if the word is a noun
    paste0("Where is he/she ",verb," the " ,word) #print the question together with the auxillary verb and the word
  }
  else{
    "The word is not a noun" #If the word is not noun it will print the same
  }
  
}

noun("touching","flower") # this will generate "Where is he/she touching the flower

