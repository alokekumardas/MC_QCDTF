
from ROOT import TH1F, TFile, TChain, TCanvas, gROOT
import ROOT
import sys
import math
import os
import os
from optparse import OptionParser
parser = OptionParser()

parser.add_option("-y", "--year", dest="Year", default="",type='str',
                     help="Specify which year %s, 2017 or 2018?" )
parser.add_option("-c", "--channel", dest="channel", default="Mu",type='str',
                     help="Specify which channel Mu or Ele? default is Mu" )

(options, args) = parser.parse_args()

gROOT.SetBatch(True)

##chan="Ele"
#year="%s"
chan=options.channel
year=options.Year
tree=TChain("AnalysisTree")
#### ALDAS for notsmeared ntuples and LPCTOP for smeared ntuples
tree.Add("root://cmseos.fnal.gov://store/user/aldas/TTGamma_FullRun2/AnalysisNtuples_Dec2020/%s/GJets_HT100To200_%s_AnalysisNtuple.root"%(year,year))
tree.Add("root://cmseos.fnal.gov://store/user/aldas/TTGamma_FullRun2/AnalysisNtuples_Dec2020/%s/GJets_HT200To400_%s_AnalysisNtuple.root"%(year,year))
tree.Add("root://cmseos.fnal.gov://store/user/aldas/TTGamma_FullRun2/AnalysisNtuples_Dec2020/%s/GJets_HT400To600_%s_AnalysisNtuple.root"%(year,year))
tree.Add("root://cmseos.fnal.gov://store/user/aldas/TTGamma_FullRun2/AnalysisNtuples_Dec2020/%s/GJets_HT40To100_%s_AnalysisNtuple.root"%(year,year))
tree.Add("root://cmseos.fnal.gov://store/user/aldas/TTGamma_FullRun2/AnalysisNtuples_Dec2020/%s/GJets_HT600ToInf_%s_AnalysisNtuple.root"%(year,year))


tree.Add("root://cmseos.fnal.gov://store/user/aldas/TTGamma_FullRun2/AnalysisNtuples_Dec2020/%s/QCD_Pt20to30_Ele_%s_AnalysisNtuple.root"%(year,year))
tree.Add("root://cmseos.fnal.gov://store/user/aldas/TTGamma_FullRun2/AnalysisNtuples_Dec2020/%s/QCD_Pt30to50_Ele_%s_AnalysisNtuple.root"%(year,year))
tree.Add("root://cmseos.fnal.gov://store/user/aldas/TTGamma_FullRun2/AnalysisNtuples_Dec2020/%s/QCD_Pt50to80_Ele_%s_AnalysisNtuple.root"%(year,year))
tree.Add("root://cmseos.fnal.gov://store/user/aldas/TTGamma_FullRun2/AnalysisNtuples_Dec2020/%s/QCD_Pt80to120_Ele_%s_AnalysisNtuple.root"%(year,year))
tree.Add("root://cmseos.fnal.gov://store/user/aldas/TTGamma_FullRun2/AnalysisNtuples_Dec2020/%s/QCD_Pt120to170_Ele_%s_AnalysisNtuple.root"%(year,year))
tree.Add("root://cmseos.fnal.gov://store/user/aldas/TTGamma_FullRun2/AnalysisNtuples_Dec2020/%s/QCD_Pt170to300_Ele_%s_AnalysisNtuple.root"%(year,year))
tree.Add("root://cmseos.fnal.gov://store/user/aldas/TTGamma_FullRun2/AnalysisNtuples_Dec2020/%s/QCD_Pt300toInf_Ele_%s_AnalysisNtuple.root"%(year,year))
tree.Add("root://cmseos.fnal.gov://store/user/aldas/TTGamma_FullRun2/AnalysisNtuples_Dec2020/%s/QCD_Pt20to30_bcToE_%s_AnalysisNtuple.root"%(year,year))
tree.Add("root://cmseos.fnal.gov://store/user/aldas/TTGamma_FullRun2/AnalysisNtuples_Dec2020/%s/QCD_Pt30to80_bcToE_%s_AnalysisNtuple.root"%(year,year))
tree.Add("root://cmseos.fnal.gov://store/user/aldas/TTGamma_FullRun2/AnalysisNtuples_Dec2020/%s/QCD_Pt80to170_bcToE_%s_AnalysisNtuple.root"%(year,year))
tree.Add("root://cmseos.fnal.gov://store/user/aldas/TTGamma_FullRun2/AnalysisNtuples_Dec2020/%s/QCD_Pt170to250_bcToE_%s_AnalysisNtuple.root"%(year,year))
tree.Add("root://cmseos.fnal.gov://store/user/aldas/TTGamma_FullRun2/AnalysisNtuples_Dec2020/%s/QCD_Pt250toInf_bcToE_%s_AnalysisNtuple.root"%(year,year))


tree1=TChain("AnalysisTree")

tree1.Add("root://cmseos.fnal.gov://store/user/aldas/TTGamma_FullRun2/AnalysisNtuples_Dec2020/QCD_controlRegion/%s/QCDcr_GJets_HT100To200_%s_AnalysisNtuple.root"%(year,year))
tree1.Add("root://cmseos.fnal.gov://store/user/aldas/TTGamma_FullRun2/AnalysisNtuples_Dec2020/QCD_controlRegion/%s/QCDcr_GJets_HT200To400_%s_AnalysisNtuple.root"%(year,year))
tree1.Add("root://cmseos.fnal.gov://store/user/aldas/TTGamma_FullRun2/AnalysisNtuples_Dec2020/QCD_controlRegion/%s/QCDcr_GJets_HT400To600_%s_AnalysisNtuple.root"%(year,year))
tree1.Add("root://cmseos.fnal.gov://store/user/aldas/TTGamma_FullRun2/AnalysisNtuples_Dec2020/QCD_controlRegion/%s/QCDcr_GJets_HT40To100_%s_AnalysisNtuple.root"%(year,year))
tree1.Add("root://cmseos.fnal.gov://store/user/aldas/TTGamma_FullRun2/AnalysisNtuples_Dec2020/QCD_controlRegion/%s/QCDcr_GJets_HT600ToInf_%s_AnalysisNtuple.root"%(year,year))


tree1.Add("root://cmseos.fnal.gov://store/user/aldas/TTGamma_FullRun2/AnalysisNtuples_Dec2020/QCD_controlRegion/%s/QCDcr_QCD_Pt20to30_Ele_%s_AnalysisNtuple.root"%(year,year))
tree1.Add("root://cmseos.fnal.gov://store/user/aldas/TTGamma_FullRun2/AnalysisNtuples_Dec2020/QCD_controlRegion/%s/QCDcr_QCD_Pt30to50_Ele_%s_AnalysisNtuple.root"%(year,year))
tree1.Add("root://cmseos.fnal.gov://store/user/aldas/TTGamma_FullRun2/AnalysisNtuples_Dec2020/QCD_controlRegion/%s/QCDcr_QCD_Pt50to80_Ele_%s_AnalysisNtuple.root"%(year,year))
tree1.Add("root://cmseos.fnal.gov://store/user/aldas/TTGamma_FullRun2/AnalysisNtuples_Dec2020/QCD_controlRegion/%s/QCDcr_QCD_Pt80to120_Ele_%s_AnalysisNtuple.root"%(year,year))
tree1.Add("root://cmseos.fnal.gov://store/user/aldas/TTGamma_FullRun2/AnalysisNtuples_Dec2020/QCD_controlRegion/%s/QCDcr_QCD_Pt120to170_Ele_%s_AnalysisNtuple.root"%(year,year))
tree1.Add("root://cmseos.fnal.gov://store/user/aldas/TTGamma_FullRun2/AnalysisNtuples_Dec2020/QCD_controlRegion/%s/QCDcr_QCD_Pt170to300_Ele_%s_AnalysisNtuple.root"%(year,year))
tree1.Add("root://cmseos.fnal.gov://store/user/aldas/TTGamma_FullRun2/AnalysisNtuples_Dec2020/QCD_controlRegion/%s/QCDcr_QCD_Pt300toInf_Ele_%s_AnalysisNtuple.root"%(year,year))
tree1.Add("root://cmseos.fnal.gov://store/user/aldas/TTGamma_FullRun2/AnalysisNtuples_Dec2020/QCD_controlRegion/%s/QCDcr_QCD_Pt20to30_bcToE_%s_AnalysisNtuple.root"%(year,year))
tree1.Add("root://cmseos.fnal.gov://store/user/aldas/TTGamma_FullRun2/AnalysisNtuples_Dec2020/QCD_controlRegion/%s/QCDcr_QCD_Pt30to80_bcToE_%s_AnalysisNtuple.root"%(year,year))
tree1.Add("root://cmseos.fnal.gov://store/user/aldas/TTGamma_FullRun2/AnalysisNtuples_Dec2020/QCD_controlRegion/%s/QCDcr_QCD_Pt80to170_bcToE_%s_AnalysisNtuple.root"%(year,year))
tree1.Add("root://cmseos.fnal.gov://store/user/aldas/TTGamma_FullRun2/AnalysisNtuples_Dec2020/QCD_controlRegion/%s/QCDcr_QCD_Pt170to250_bcToE_%s_AnalysisNtuple.root"%(year,year))
tree1.Add("root://cmseos.fnal.gov://store/user/aldas/TTGamma_FullRun2/AnalysisNtuples_Dec2020/QCD_controlRegion/%s/QCDcr_QCD_Pt250toInf_bcToE_%s_AnalysisNtuple.root"%(year,year))


h41=TH1F("h41","h41",1,0,2)
h41.Sumw2()
tree.Draw("1 >> h41","(passPresel_Ele && nJet>=4 && nBJet>=1 && nPho==0 && nLoosePho==0)*evtWeight*PUweight*eleEffWeight*btagWeight_1a*prefireSF")
QCD14=h41.GetBinContent(1)
QCD14err=h41.GetBinError(1)
h42=TH1F("h42","h42",1,0,2)
h42.Sumw2()
tree1.Draw("1 >> h42","(passPresel_Ele && nJet>=4 && nBJet==0 && nPho==0 && nLoosePho==0 )*evtWeight*PUweight*eleEffWeight*btagWeight_1a*prefireSF")
QCD24=h42.GetBinContent(1)
QCD24err=h42.GetBinError(1)
QCDTF4=QCD14/QCD24
QCDTFError4=QCDTF4*math.sqrt(pow((QCD14err/QCD14),2) +pow( (QCD24err/QCD24),2))
print "SR=",QCD14, "CR=",QCD24
print "QCDTF41%s%s="%(chan,year),QCDTF4
print "QCDTFError41%s%s="%(chan,year),QCDTFError4


h31=TH1F("h31","h31",1,0,2)
h31.Sumw2()
tree.Draw("1 >> h31","(passPresel_Ele && nJet==3 && nBJet>=1 && nPho==0 && nLoosePho==0)*evtWeight*PUweight*eleEffWeight*btagWeight_1a*prefireSF")
QCD13=h31.GetBinContent(1)
QCD13err=h31.GetBinError(1)
h32=TH1F("h32","h32",1,0,2)
h32.Sumw2()
tree1.Draw("1 >> h32","(passPresel_Ele && nJet==3 && nBJet==0 && nPho==0 && nLoosePho==0)*evtWeight*PUweight*eleEffWeight*btagWeight_1a*prefireSF")
QCD23=h32.GetBinContent(1)
QCD23err=h32.GetBinError(1)
QCDTF3=QCD13/QCD23
QCDTFError3=QCDTF3*math.sqrt(pow((QCD13err/QCD13),2) +pow( (QCD23err/QCD23),2))
print "SR=",QCD13,"CR=",QCD23
print "QCDTF31%s%s="%(chan,year),QCDTF3
print "QCDTFError31%s%s="%(chan,year),QCDTFError3

h21=TH1F("h21","h21",1,0,2)
tree.Draw("1 >> h21","(passPresel_Ele && nJet==2 && nBJet>=1 && nPho==0 && nLoosePho==0)*evtWeight*PUweight*eleEffWeight*btagWeight_1a*prefireSF")
QCD12=h21.GetBinContent(1)
QCD12err=h21.GetBinError(1)
h22=TH1F("h22","h22",1,0,2)
tree1.Draw("1 >> h22","(passPresel_Ele && nJet==2 && nBJet==0 && nPho==0 && nLoosePho==0 )*evtWeight*PUweight*eleEffWeight*btagWeight_1a*prefireSF")
QCD22=h22.GetBinContent(1)
QCD22err=h22.GetBinError(1)
QCDTF2=QCD12/QCD22
QCDTFError2=QCDTF2*math.sqrt(pow((QCD12err/QCD12),2) +pow( (QCD22err/QCD22),2))
print "SR=",QCD12,"CR=",QCD22
print "QCDTF21%s%s="%(chan,year),QCDTF2
print "QCDTFError21%s%s="%(chan,year),QCDTFError2

