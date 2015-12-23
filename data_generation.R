setwd("C:/Users/Yan/Desktop/Stony_Brook_courses/AMS691/group_proj/US-market")
csvarray=list.files(path="C:/Users/Yan/Desktop/Stony_Brook_courses/AMS691/group_proj/US-market")

#select one for each month
selected_indice=c(1,10,59,91,119,149)
summary_df=NULL
for(i in selected_indice){
  input_df=read.csv(csvarray[i])
  if(is.null(summary_df)){
    summary_df=input_df[,c(1,2)]
    summary_df$Global.Monthly.Searches=as.numeric(as.character(summary_df$Global.Monthly.Searches))
    summary_df$Global.Monthly.Searches[which(is.na(summary_df$Global.Monthly.Searches))]=0
  }else{
    if(mean(summary_df$Keyword==input_df$Keyword)!=1){
      print("error in names")
      break
    }
    input_df$Global.Monthly.Searches=as.numeric(as.character(input_df$Global.Monthly.Searches))
    input_df$Global.Monthly.Searches[which(is.na(input_df$Global.Monthly.Searches))]=0
    summary_df$Global.Monthly.Searches=summary_df$Global.Monthly.Searches+input_df$Global.Monthly.Searches
  }
}
hist(summary_df$Global.Monthly.Searches,breaks=100)
hist(log10(summary_df$Global.Monthly.Searches),breaks=100)

###############key word frequency done############
summary_df$keyword_freq=summary_df$Global.Monthly.Searches/sum(summary_df$Global.Monthly.Searches)
###################initialization#################
advister_df=data.frame(id=c(1:10000))
for(i in 1:547){
  advister_df[,i+1]=0
  colnames(advister_df)[i+1]=paste("keyword",i,sep="")
}
############generate budget################
#add random base to avoid unreasonably low budget
advister_df$budget=round(rexp(10000,1/5000))+sample(200:500,10000,replace=T)
############generate keywords number based on budget##############
advister_df$keyword_count=rpois(10000,lambda=advister_df$budget/500)+2
range(advister_df$keyword_count)
############generate specific keywords based on keyword number########
for(i in 1:10000){
  #sample based on keyword frequency as probability
  #plus 1 because column 1 is id
  advister_df[i,sample(547,size=advister_df$keyword_count[i],prob=summary_df$keyword_freq)+1]=1
}
#check the number of keywords is right
mean(rowSums(advister_df[,c(2:548)])==advister_df$keyword_count)
#check the distribution of keywords matches the probability
new_obs=colSums(advister_df[,c(2:548)])#/sum(advister_df$keyword_count)
ks.test(new_obs,"rmultinom",size=sum(advister_df$keyword_count),prob=summary_df$keyword_freq)
#########do not reject#############
write.csv(advister_df,"advister_info.csv",row.names=FALSE)


###################generate query###############
#generate a sequence of coming key words
query_array=rmultinom(n=1e6,size=547,prob=summary_df$keyword_freq)
query_array=rep(0,1e6)
for(i in 1:1e6){
  query_array[i]=which(rmultinom(n=1,size=1,prob=summary_df$keyword_freq)==1)
  if(i%%1e5==0){
    print(i)
  }
}
write.csv(query_array,"query_key.csv",row.names=FALSE)
