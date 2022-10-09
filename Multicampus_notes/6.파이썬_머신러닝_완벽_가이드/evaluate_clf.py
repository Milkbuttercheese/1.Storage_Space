from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix ,f1_score,roc_auc_score,precision_recall_curve,roc_curve
from sklearn.preprocessing import Binarizer,StandardScaler
import numpy as np 
import matplotlib.pyplot as plt 

def get_clf_eval(y_test,y_pred):
    confusion= confusion_matrix(y_test,y_pred)
    accuracy = accuracy_score(y_test,y_pred)
    precision= precision_score(y_test,y_pred)
    recall= recall_score(y_test,y_pred)
    print('오차 행렬')
    print(confusion)
    print(f'정확도 {accuracy:.3f} 정밀도 {precision:.3f} 재현율 {recall:.3f} ')


def get_clf_eval2(y_test,y_pred=None,pred_proba=None):
    confusion= confusion_matrix(y_test,y_pred)
    accuracy= accuracy_score(y_test,y_pred)
    precision= precision_score(y_test,y_pred)
    recall= recall_score(y_test,y_pred)
    f1= f1_score(y_test,y_pred)
    #ROC-AUC 추가
    roc_auc = roc_auc_score(y_test,pred_proba)
    print('오차 행렬')
    print(confusion)
    #ROC-AUC print 추가
    print(f' 정확도는 {accuracy:.3f} 정밀도는 {precision:.3f} \
    재현율은 {recall:.3f} F1는 {f1:.3f}, AUC는 {roc_auc:.3f} 이다')


def get_eval_by_threshold(y_test,pred_proba_c1,thresholds):
    for custom_threshold in thresholds:
        binarizer= Binarizer(threshold=custom_threshold).fit(pred_proba_c1) 
        custom_predict= binarizer.transform(pred_proba_c1)
        print('------------------------------------------------------')
        print(f'임계값 {custom_threshold}')
        get_clf_eval(y_test,custom_predict)


def roc_curve_plot(y_test,pred_proba_c1):
    fprs, tprs, thresholds= roc_curve(y_test,pred_proba_c1)
    #ROC 곡선을 그래프 곡선으로 그린다
    plt.plot(fprs,tprs,label='ROC')
    #가운데 대각선 직선을 그린다
    plt.plot([0,1],[0,1],'k--',label='random')

    # FPR X 축의 scale을 0.1 단위로 변경. X축 Y축명 설정등
    start, end = plt.xlim()
    plt.xticks(np.round(np.arange(start,end,0.1),2))
    plt.xlim(0,1); plt.ylim(0,1)
    plt.xlabel('FPR(1-Sensitivity'); plt.ylabel('TPR(Recall)')
    plt.legend()


def precision_recall_curve_plot(y_test,pred_proba_c1):
    precisions, recalls, thresholds = precision_recall_curve(y_test,pred_proba_c1)

    #X 축을 threshold 값으로, y값을 정밀도,재현율 값으로 각각 plot을 수행한다. 정밀도는 점선으료 표시한다
    plt.figure(figsize=(8,6))
    threshold_boundary= thresholds.shape[0]
    plt.plot(thresholds,precisions[0:threshold_boundary],linestyle='--',label='precision')
    plt.plot(thresholds,recalls[0:threshold_boundary],label='recall')

    #threthreshold 값 X축의 scale을 0.1 단위로 변경한다
    start,end = plt.xlim()
    plt.xticks(np.round(np.arange(start,end,0.1),2))

    #x축,y축, label, legend, 그리고 grid를 설정한다
    plt.xlabel('Threshold value'); plt.ylabel('Precision and Recall value')
    plt.legend() ; plt.grid()
    plt.show()



#클래스 버전
# class eval_clf:
#     def __init__(self,y_test,pred,pred_proba_c1,thresholds):
#         self.y_test=y_test 
#         self.pred= pred 
#         self.pred_proba_c1= pred_proba_c1
#         self.thresholds= thresholds


#     def get_clf_eval(self):
#         confusion= confusion_matrix(y_test,pred)
#         accuracy = accuracy_score(y_test,pred)
#         precision= precision_score(y_test,pred)
#         recall= recall_score(y_test,pred)
#         print('오차 행렬')
#         print(confusion)
#         print(f'정확도 {accuracy:.3f} 정밀도 {precision:.3f} 재현율 {recall:.3f} ')


#     def get_eval_by_threshold(self):
#         for custom_threshold in thresholds:
#             binarizer= Binarizer(threshold=custom_threshold).fit(pred_proba_c1) 
#             custom_predict= binarizer.transform(pred_proba_c1)
#             print(f'임계값 {custom_threshold}')
#             get_clf_eval(y_test,custom_predict)